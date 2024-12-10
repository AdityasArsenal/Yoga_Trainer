                statues_of_left_hand = left_hand_check(lm11,lm13,lm15)
                if statues_of_left_hand :
                    statues_of = right_leg_check(lm24,lm26,lm28)
                
                if statues_of:
                    statues_of = left_leg_check(lm23,lm25,lm27)
            
                if statues_of:
                    statues_of = right_hip_check(lm12,lm24,lm26)
        
                if statues_of:
                    statues_of = left_hip_check(lm11,lm23,lm25)
    
                if statues_of:
                    print("correct pose")