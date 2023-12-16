#!/usr/bin/env node

import fs from "fs/promises"
import path from "path"

import puppeteer from "puppeteer"
import express from "express"

const parseDataUrl = url => {
  const match = url.match(/^data:image\/png;base64,(.+)$/)
  if (!match) {
    throw new Error(`Could not parse data URL: ${JSON.stringify(url)}`)
  }
  return Buffer.from(match[1], "base64")
}

class Renderer {
  constructor() {
    this.scale = 2
  }

  async start() {
    const app = express()
    app.use(express.static("."))
    await new Promise(resolve => {
      this.server = app.listen(8002, resolve)
    })
    this.browser = await puppeteer.launch({
      //headless: false,
      //slowMo: 250,
    })
    this.page = await this.browser.newPage()
    this.page.on("pageerror", e => {
      throw new Error("Page threw uncaught exception", { cause: e })
    })
    this.page.on("console", msg => console.log(msg.type(), ":", msg.text()))

    await this.page.goto(
      "http://localhost:8002/snapshots/snapshot-testing.html",
    )
    await this.page.waitForFunction("window.scratchblocksLoaded")
  }

  async snapshot(script, options) {
    const args = [script, options, this.scale]
      .map(x => JSON.stringify(x))
      .join(", ")
    const dataURL = await this.page.evaluate(`render(${args})`)
    try {
      return parseDataUrl(dataURL)
    } catch (e) {
      throw new Error(`Could not render script ${args}`, { cause: e })
    }
  }

  async snapshotToFile(script, options, fpath) {
    const buffer = await this.snapshot(script, options, this.scale)
    await fs.mkdir(path.dirname(fpath), { recursive: true })
    await fs.writeFile(fpath, buffer)
  }

  async stop() {
    await this.browser.close()
    if (this.server) {
      this.server.close()
    }
  }
}

export default new Renderer()
