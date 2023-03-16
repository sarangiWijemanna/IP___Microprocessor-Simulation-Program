
# Microprocessor Simulation Program 📑📌📝

## Basic idea Of Microprocessor
 <img src="basic idea behind the uC.png" />

## Objective
Designed a python program for instruction decoder to decode machine code back to the assembly program and developed a microprocessor simulation program for the given custom instruction set.

## Operations

| **Description**                                                                                   | **Instruction** |
|---------------------------------------------------------------------------------------------------|:---------------:|
| No-Operation ---> NOP;                                                                            |       NOP       |
| Add instruction ---> ADD RS, RD, RT;                                                              |       ADD       |
| Add Immediate instruction ---> ADDI RS, RD, Imm;                                                  |      ADDI       |
| Subtract instruction ---> SUB RS, RD, RT;                                                         |       SUB       |
| Subtract Immediate instruction ---> SUBI RS, RD, Imm;                                             |      SUBI       |
| Load instruction ---> LOAD RS, RD;                                                                |      LOAD       |
| Store instruction ---> STORE RS, RT;                                                              |      STORE      |
| Bitwise-And instruction ---> AND RS, RD, RT;                                                      |       AND       |
| Bitwise-Or instruction ---> OR RS, RD, RT;                                                        |       OR        |
| Bitwise-Not instruction ---> NOT RS, RD;                                                          |       NOT       |
| Bitwise-Xor instruction ---> XOR RS, RD, RT;                                                      |       XOR       |
| Bitwise-AND-Immediate instruction ---> ANDI RS, RD, Imm;                                          |      ANDI       |
| Bitwise-OR-Immediate instruction ---> ORI RS, RD, Imm;                                            |       ORI       |
| Logical-Left-Shift instruction ---> LLSHIFT RS, RD, Cnt;                                          |     LLSHIFT     |
| Logical-Right-Shift instruction ---> LRSHIFT RS, RD, Cnt;                                         |     LRSHIFT     |
| Arithmetic-Left-Shift instruction ---> ALSHIFT RS, RD, Cnt;                                       |     ALSHIFT     |
| Arithmetic-Right-Shift instruction ---> ARSHIFT RS, RD, Cnt;                                      |     ARSHIFT     |
| Branch-Unconditional instruction ---> BRAUNCOND Imm2, Imm;                                        |    BRAUNCOND    |
| Branch-on-Zero instruction ---> BRAZ Imm2, Imm;                                                   |      BRAZ       |
| Branch-on-Carry instruction ---> BRAC Imm2, Imm;                                                  |      BRAC       |
| Branch-on-Overflow instruction ---> BRAV Imm2, Imm;                                               |      BRAV       |
| Load-Internal instruction ---> LOADI RS, RD;                                                      |      LOADI      |
| Store-Internal instruction ---> STOREI RS, RT;                                                    |     STOREI      |
| ?                                                                                                 |      HALT       |
| Branch-Register instruction ---> BRAREG RT;                                                       |     BRAREG      |
| Branch-on-Not-Zero instruction ---> BRANZ Imm2, Imm;                                              |      BRANZ      |
| Branch-on-Greater-Than-Zero instruction ---> BRAGEZ Imm2, Imm;                                    |     BRAGEZ      |
| Branch-on-Less-Than-Zero instruction ---> BRALEZ Imm2, Imm;                                       |     BRALEZ      |
| Move instruction ---> MOV Imm2, RD, Imm;                                                          |       MOV       |
| Logical-Left-Register-Shift instruction ---> LLSHIFTREG RS, RD, RT;                               |   LLSHIFTREG    |
| Logical-Right-Register-Shift instruction ---> LRSHIFTREG RS, RD, RT;                              |   LRSHIFTREG    |


## Note

 &nbsp; **Hidden Files** :   ```Processor.py``` ```insdecorder.py ```
                             
## Tech Stack  
<table>
        <td align="center" width="96">
          <a href="#macropower-tech">
            <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="65" height="65" />
          </a>
          <br>Python
        </td>
</table>
          
## Authors

- [@SasanthaR](https://github.com/SasanthaR)                                                                                                        
 
  [//]: contributor-faces
 <a href="https://github.com/ngryman"><img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/105480277?v=4&h=100&w=100&fit=cover&mask=circle&maxage=4d"></a>
  
 

## Suggestions

Don't forget to leave feedback if you find this repo useful or any improvements⭐

Thank you 🧡

    
