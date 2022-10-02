if :vara < :varb [
   
   repeat 10 [
      :vara = :vara + 1
      repeat 3 [
         :vara = :vara + 1
		 right 30
		 forward :vara
      ]
	  backward :vara
   ]
]
else [
	forward :vara
]