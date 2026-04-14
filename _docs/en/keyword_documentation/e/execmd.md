---
lang: en
title: "EXECMD (2D3D)"
---

# EXECMD

|  (Action keyword)  
---|---  
_Update History:_ (New) Definition has been updated v11 |  Last updated on : 30-07-2013  
  
* * *

EXECMD Opt

Command

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Opt |  Type of program =**0** DEFORM executables =**1** System executables =**2** DEFORM 2D executable (new in v11) =**3** DEFORM 3D executable (new in v11) |  0  
Command |  The command to execute |  none  
  
DEFINITION  
---  
EXECMD executes either a program in the DEFORM executable directory or a system command. This is mainly used in Multiple Operation, where by specifying this keyword in the Master file (.MST), a separate program can be executed.  
  
REMARKS  
---  
This keyword is mainly for internal use. The DEFORM executable directory is $DEFORM3_DIR/EXE on UNIX. Some arguments may be specified for the program. The maximum length of the command line is 200.  
  
RELATED TOPICS  
---  
[Pre-processor](/docs/en/pre_processor/7_introduction_to_pre-processor/)
