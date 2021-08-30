def fight(robot_1, robot_2, tactics):
    player=True if robot_1["speed"]>=robot_2["speed"] else False
    index1=0
    index2=0
    while index1<len(robot_1["tactics"]) or index2<len(robot_2["tactics"]):
        if player:
            if index1<len(robot_1["tactics"]):  
                robot_2["health"]-=tactics[robot_1["tactics"][index1]]
                index1+=1
            if robot_2["health"]<=0:
                return robot_1["name"]+" has won the fight."
            if index2<len(robot_2["tactics"]):  
                robot_1["health"]-=tactics[robot_2["tactics"][index2]]
                index2+=1
            if robot_1["health"]<=0:
                return robot_2["name"]+" has won the fight."
        else:
            if index2<len(robot_2["tactics"]):  
                robot_1["health"]-=tactics[robot_2["tactics"][index2]]
                index2+=1
            if robot_1["health"]<=0:
                return robot_2["name"]+" has won the fight."
            if index1<len(robot_1["tactics"]):  
                robot_2["health"]-=tactics[robot_1["tactics"][index1]]
                index1+=1
            if robot_2["health"]<=0:
                return robot_1["name"]+" has won the fight."
    return robot_1["name"]+" has won the fight." if robot_1["health"]>robot_2["health"] else 'The fight was a draw.' if robot_2["health"]==robot_1["health"] else robot_2["name"]+" has won the fight."