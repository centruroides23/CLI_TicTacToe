TICTACTOE = """
  A     B     C
      |     |     
1  .  |  .  |  .  
 _____|_____|_____
      |     |     
2  .  |  .  |  .  
 _____|_____|_____
      |     |     
3  .  |  .  |  .  
      |     |     
"""

SPACE_MAP = {
            39: "A1", 45: "B1", 51: "C1",
            96: "A2", 102: "B2", 108: "C2",
            153: "A3", 159: "B3", 165: "C3"
            }

WIN_CONDITIONS = {
    "condition_1": [39, 45, 51],
    "condition_2": [96, 102, 108],
    "condition_3": [153, 159, 165],
    "condition_A": [39, 96, 153],
    "condition_B": [45, 102, 159],
    "condition_C": [51, 108, 165],
    "condition_R": [39, 102, 108],
    "condition_L": [153, 102, 51],
}