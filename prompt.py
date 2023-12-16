SCRATCH_KNOWLEDGE = """
This article demonstrates the Block Plugin syntax.

On the Scratch Forums, code must be written between [scratchblocks]...[/scratchblocks] tags. (On the wiki, <scratchblocks>...</scratchblocks> tags are used.) For a simplified explanation, see here.

Every block goes on a new line and is written as the text on the block is shown on Scratch. For example:

Code	Result
[scratchblocks]
when green flag clicked
forever
    turn cw (15) degrees
    say [Hello!] for (2) seconds
    if <mouse down?> then
        change [mouse clicks v] by (1)
    end
end
[/scratchblocks]
when green flag clicked
forever
    turn cw (15) degrees
    say [Hello!] for (2) seconds
    if <mouse down?> then
        change [mouse clicks v] by (1)
    end
end

Contents
1	Arguments
1.1	Numerical Insert
1.2	String Insert
1.3	Block Insert
1.4	Color Input
1.5	Dropdown List
2	Special Blocks
2.1	Hat Blocks
2.2	Stack Blocks
2.3	C Blocks
3	Comments
4	Custom Blocks
4.1	Custom Block Inputs
5	List Reporters
6	Shortening Source Code
7	Hacks
7.1	Color and Shape Changing
7.2	Snap!
7.3	GP
8	Backslash
Arguments
Arguments, or inputs to a block, are represented within the block with various codes.

Numerical Insert
The round numerical insert is used with parentheses: (10).

move (10) steps
move (10) steps
String Insert
String inputs are created with square brackets: [lorem ipsum]

say [Hi]
say [Hi]
think [bye]
think [bye]
Block Insert
Boolean blocks and reporter blocks are created with <boolean> and (reporter), respectively.

if <<mouse down?> and <(costume [number v]) = [1]>> then
    stamp
end
if <<mouse down?> and <(costume [number v]) = [1]>> then
    stamp
end
Boolean blocks used to appear round, like reporters, but this was corrected with scratchblocks3.

Color Input
Color inputs can be made by entering a hexadecimal code into a string input.

set pen color to [#1540bf]
set pen color to [#1540bf]
Note that 3-byte long hexadecimal codes are also supported.

set pen color to [#0f0]
set pen color to [#0f0]
Dropdown List
Dropdown lists are created with the code [selection v].

stop [all v]
stop [all v]
Round dropdowns are created with (selection v).

broadcast (start v)
broadcast (start v)
Special Blocks
Some blocks have different code based on their unique shapes and features.

Hat Blocks
The When Green Flag Clicked block can be typed with any of the following syntax options:

when green flag clicked
when gf clicked
when flag clicked
when gf clicked
For the When () Clicked block, the old block plugin required the sprite's name to be surrounded by brackets. This is no longer necessary:

when this sprite clicked
when this sprite clicked
Stack Blocks
The Turn () Degrees (clockwise) block can be written two ways:

turn cw () degrees
turn right () degrees
turn cw () degrees
The Turn () Degrees (counter-clockwise) block can also be written two ways:

turn ccw () degrees
turn left () degrees
turn ccw () degrees
C Blocks
C blocks must be closed by typing "end" after the last stack block inside it. However, C blocks at the end of a script will close automatically. For example:

repeat (10)
    move (5) steps
    stamp
end
repeat (10)
    move (10) steps
    stamp
Makes:

repeat (10)
    move (5) steps
    stamp
end
repeat (10)
    move (10) steps
    stamp
Comments
Comments are created with two slashes: // comment after a block.

move (10) steps // is that too far?
move (10) steps // is that too far?
Custom Blocks
If one tries to show a custom block, it will appear obsolete (red) because it has not been defined.

jump
jump
A definition can be created by writing "define" followed by the name of the block:

define jump
repeat (10)
    change y by (4)
end
define jump
repeat (10)
    change y by (4)
end
Number, boolean, and string arguments can be added:

define jump (height) <gravity on?> [message]
define jump (height) <gravity on?> [message]
Once a define hat has been made, one can then use the block inside the same <scratchblocks> tag, and it will no longer appear obsolete.

jump

define jump
repeat (10)
    change y by (4)
end
jump

define jump
repeat (10)
    change y by (4)
end
Custom Block Inputs
If one tries to use an input reporter without making a block definition first, it will appear as a variable.

say (height)
say (height)
But if it is put below a block definition, it will render as an input reporter:

define jump (height)
say (input)
define jump (height)
say (height)
List Reporters
If one tries to write a list reporter, it will look like a variable reporter, because the plugin has no way of telling them apart.

say (list of Scratch team members)
say (list of Scratch team members)
However, if one has used the list in a list block inside the same <scratchblocks> tag, then it will render correctly:

add [mres] to [list of Scratch team members v]
add [paddle2see] to [list of Scratch team members v]
add [harakou] to [list of Scratch team members v]
say (list of Scratch team members)
add [mres] to [list of Scratch team members v]
add [paddle2see] to [list of Scratch team members v]
add [harakou] to [list of Scratch team members v]
say (list of Scratch team members)
If a list block is not wanted or needed inside the same <scratchblocks> tag, :: list can be used:

say (list of Scratch team members:: list)
say (list of Scratch team members:: list)
Shortening Source Code
It is possible to make the source of ScratchBlocks code slightly shorter by removing unnecessary code. No spaces are necessary between an insert and the block text. Also, closing brackets (]) and parentheses ()) can be left off at the end of a line. Therefore, the following two snippets render identically, though the first is 226 characters, and the second only 183:

when gf clicked
ask [n=] and wait
set [n v] to (answer)
set [i v] to [0]
repeat until <(n) = [1]>
if <((n) mod (2)) = [0]> then
set [n v] to ((n) / (2))
else
set [n v] to (((3) * (n)) + (1))
end
change [i v] by (1)
end
say (i)
when gf clicked
ask[n=]and wait
set[n v]to(answer
set[i v]to[0
repeat until<(n)=[1
if<((n)mod(2))=[0]>then
set[n v]to((n)/(2
else
set[n v]to(((3)*(n))+(1
end
change[i v]by(1
end
say(i
when gf clicked
ask[n=]and wait
set[n v]to(answer
set[i v]to[0
repeat until<(n)=[1
if<((n)mod(2))=[0]>then
set[n v]to((n)/(2
else
set[n v]to(((3)*(n))+(1
end
change[i v]by(1
end
say(i
However, this is considered poor style and is not recommended.

Hacks
The blocks plugin offers hacks to allow representation of scripts from Scratch Modifications and old or unreleased versions of Scratch.

For a full tutorial on how to use scratchblocks hacks, see this topic.

Color and Shape Changing
The color and shape of a block can be changed. This can be useful for forcing non-Scratch blocks to appear correctly. Note that only color changing with the legacy syntax works in the old version. The legacy syntax is obsolete (it no longer works since scratchblocks3).

Feature	Code	Result
Changing category (works for any kind of block)	
abc:: looks
say [I'm not a Motion block!]:: motion
eat (pen color:: pen):: control
if <touching (mouse pointer v)?:: list> then
    die:: grey
end
abc:: looks
say [I'm not a Motion block!]:: motion
eat (pen color:: pen):: control
if <touching (mouse pointer v)?:: list> then
    die:: grey
end
Changing color	
think [Arbitrary colors?]:: #228b22
think [Arbitrary colors?]:: #228b22
Changing shape	
abc:: events hat
def:: motion stack
ghi:: pen reporter
jkl:: operators boolean
abc:: events hat
def:: motion stack
ghi:: pen reporter
jkl:: operators boolean
Creating C blocks and changing category	
mno {{
    ...
}}:: sensing
mno {{
    ...
}}:: sensing
C blocks with multiple branches	
pqr {{
    ...
}} stu {{
    ...
}} vwx:: sound
pqr {{
    ...
}} stu {{
    ...
}} vwx:: sound
C block with cap	
yz {{
    ...
}}:: motion cap
yz {{
    ...
}}:: motion cap
Adding icons	
@greenFlag @stopSign @turnRight @loopArrow:: grey
@greenFlag @stopSign @turnRight @loopArrow:: grey
Snap!
See also: Snap!

The new plugin also supports features specific to Snap!, such as "rings". Other blocks in Snap! can be created using the color/shape hacks above.

run ({{create clone:: control}} @addInput:: grey ring):: control

<() @addInput:: grey ring>

say (http:// [snap.berkeley.edu]:: sensing)

((6) × (7):: operators)

(join [hello ] [world] @delInput @addInput:: operators)

script variables ((foo):: grey) ((bar):: grey) @delInput @addInput:: grey

warp {{
  move (10) steps
}} :: grey

report [Done!]:: control cap

(<> @addInput) // without even the:: grey ring
which produces these blocks:

run ({{create clone:: control}} @addInput:: grey ring) :: control

<() @addInput:: grey ring>

say (http:// [snap.berkeley.edu]:: sensing)

((6) × (7):: operators)

(join [hello ] [world] @delInput @addInput:: operators)

script variables ((foo):: grey) ((bar):: grey) @delInput @addInput:: grey

warp {{
  move (10) steps
}}:: grey

report [Done!]:: control cap

(<> @addInput) // without even the:: grey ring
GP
This plugin also includes hacks to GP.

when tracking (mouse x:: variables) (mouse y:: variables):: hat control

((1) !=\ (0):: operators)

define(a function:: motion):: custom hat
return (1):: control

say (pi:: operators):: motion

when I receive [go]:: control

wait @addInput:: control

(isNil [obj v]:: operators)

(touching mouse:: sensing)

((--(:: #fff):: operators):: operators)

if (--(:: #fff):: operators) {{
}} @addInput:: control
Backslash
A backslash (\) is a character that cancels out any special functionality of the next character, making it show up as normal text. If a character with special functionality, like a closing bracket (]), needs to be rendered as normal text, put a backslash before it.

say []]
say []]
say [\]]
say [\]]
This is useful in certain situations, where backslashes are necessary to properly display a block:

play drum (\(1\) Snare Drum v) for (0.25) beats
play drum (\(1\) Snare Drum v) for (0.25) beats
"""

CODE_AGENT_PROMPTV1 = """
Hi, here is the knowledge about how to write the scratch code to represent
the visual programming language:
{knowledge}. 

Now, follow this knowledge to write the code. And respond in json format with:
{{
'code': 'your code'
}}

"""
