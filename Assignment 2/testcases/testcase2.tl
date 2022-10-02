:vara = 10
:varb = 20
:vara = :varb
:a = 2
:b = 3
:a=3


if :a <= 0 [
   :x = 2 * :a
   :y = 2 * :b
]

if :vara < :varb [
   :vara = 0
   :varb = 0
]

if :vara < :varb [
   :vara = 0
   :varb = 0	
   repeat 10 [  
      :vara = 0
      :varb = 0
      repeat 10 [
         :vara = 0
         :varb = 0
      ]
   ]
]


