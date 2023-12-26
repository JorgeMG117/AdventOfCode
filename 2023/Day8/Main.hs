
--RL
--
--AAA = (BBB, CCC)
--BBB = (DDD, EEE)
--CCC = (ZZZ, GGG)
--DDD = (DDD, DDD)
--EEE = (EEE, EEE)
--GGG = (GGG, GGG)
--ZZZ = (ZZZ, ZZZ)



-- Function that recieves a node and an instruction
--   check if node is ZZZ
--   if not, go to node based on instruction
--   return 1 + call function with new node and new instruction
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * ( factorial ( n - 1 ) )

findWay :: () Lista 
  head lista
  lo metemos por la tail
  esa es la lista de instrucciones

main = do
    -- Read file input
    input <- readFile "example.txt"
    putStrLn input
    print(factorial(4))


    
