# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 5A Activity 2
# Date:         September 29, 2021

reference = [ # I'm gonna be honest this is probably the worst way to do this but I'm tired and it works so...
  [ # Male
    [
      [-9,-4,0,3,6,8,10,11,12,13], # Age modifier
      [ # Cholesterol
        [0,4,7,9,11], # 20-39
        [0,3,5,6,8], # 40-49
        [0,2,3,4,5], # 50-59
        [0,1,1,2,3], # 60-69
        [0,0,0,1,1], # 70+ ig
      ],
      [ # Smoking?
        [0,8], # 20-39
        [0,5], # 40-49
        [0,3], # 50-59
        [0,1], # 60-69
        [0,1], # 70+ ig
      ],
      [-1,0,1,2], # HDL
      [ # Blood Pressure
        [0,1,2,2,3], # Treated
        [0,0,1,1,2], # Untreated
      ],
      { # Point Thresholds
        -1:"<1",
        4:"1",
        6:"2",
        7:"3",
        8:"4",
        9:"5",
        10:"6",
        11:"8",
        12:"10",
        13:"12",
        14:"16",
        15:"20",
        16:"25",
        100:">30",
      }
    ]
  ],
  [ # Female
    [
      [-7,-3,0,3,6,8,10,12,14,16], # Age modifier
      [ # Cholesterol
        [0,4,8,11,13], # 20-39
        [0,3,6,8,10], # 40-49
        [0,2,4,5,7], # 50-59
        [0,1,2,3,4], # 60-69
        [0,1,1,2,2], # 70+ ig
      ],
      [ # Smoking?
        [0,9], # 20-39
        [0,7], # 40-49
        [0,4], # 50-59
        [0,2], # 60-69
        [0,1], # 70+ ig
      ],
      [-1,0,1,2], # HDL
      [ # Blood Pressure
        [0,3,4,5,6], # Treated
        [0,1,2,3,4], # Untreated
      ],
      { # Point Thresholds
        8:"<1",
        12:"1",
        14:"2",
        15:"3",
        16:"4",
        17:"5",
        18:"6",
        19:"8",
        20:"11",
        21:"14",
        22:"17",
        23:"22",
        24:"27",
        100:">30",
      }
    ]
  ],
]