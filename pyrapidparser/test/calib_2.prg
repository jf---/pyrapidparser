
MODULE ODC_hotwirez

    PERS tooldata hotwirez := [ TRUE, [ [ 0.000, 0.000, 733.000 ], [ 1.000000000, 0.000000000, 0.000000000, 0.000000000 ] ], [ 10.0, [ 0.040, 0.000, 733.000 ], [ 1, 0, 0, 0 ], 0, 0, 0 ] ];
    PERS pos Pos_Offset := [ 0, 0, 0 ];
    PERS speeddata cur_vel := [ 200.0, 200.0, 1000.0, 1000.0 ];
    PERS zonedata cur_zone := [FALSE, 1, 1, 50, 0.1, 50, 0.1];
    PERS wobjdata cur_wobj := [ FALSE, TRUE, "", [ [ -0.000, -0.000, -1400.000 ], [ 1.000000000, 0.000000000, 0.000000000, 0.000000000 ] ], [ [0, 0, 0], [1, 0, 0 ,0] ] ];
    PROC main()
        ! crank up the path resolution to increase toolpath precision
        PathResol 50;
        ! set the acceleration
        AccSet 100, 50;
        ! state: the robot performing a task
        ODC_RobBusy cnstNoStepIn;
        TPWrite "running with coordinated track motion...";
        ! compute the difference from the "hotwirez" tooldata in PyRAPID
        ! from the "hotwirez" tooldata on the controller
        ! inform the operator of the difference between these definitions
        ! finally, swap the "hotwirez" tooldata for the one found on the controller
        ! as a result this file is still valid when re-calibrating the tool
        !ODC_Validation \Tool:=hotwirez;
        ! performs a toolchange when the end-effector currently loaded does not match the requested process
        ! cnstPC_Process1 is the hotwirez cutting process
        !
        ODC_TC_Req_Auto \Process:=cnstPC_Process1; ! cutting
        ! need to check
        ODC_ProcSpeed cur_vel;
        ! need to check
        ODC_ProcOn cnstNoStepIn;
        ! run the toolpath
        run;
        ! need to check
        ODC_ProcOff cnstNoStepIn;
        ! state: the robot is no longer performing a task
        ODC_RobReady cnstNoStepIn;
    ENDPROC

    ! generated from CAD file: /Users/Permadsen/Desktop/calib_2.stp
    ! shell name: calib_x
    PROC calib_x( string strNoStepIn )
        ! <<< group name: grouped_faces_000 >>>
        ! ruled surface 001
        MoveL [[ 476.0, -1533.0, 1023.0 ],[ 0.000000, 0.999864, 0.000000, -0.016478 ],[-1, -1, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ 476.0, -1533.0, 998.0 ],[ 0.000000, 0.999864, 0.000000, -0.016478 ],[-1, -1, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ 476.0, -1533.0, 973.0 ],[ 0.000000, 0.999864, 0.000000, -0.016478 ],[-1, -1, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        ODC_ProcOff cnstNoStepIn;
        TPWrite "robot is paused because:";
        Stop;
        ODC_ProcOn cnstNoStepIn;
        ! ruled surface 003
        MoveL [[ -274.0, -1533.0, 973.0 ],[ -0.000000, 0.999864, 0.000000, -0.016478 ],[-2, -1, -4, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ -1024.0, -1533.0, 973.0 ],[ -0.000000, 0.999864, 0.000000, -0.016478 ],[-2, -1, -4, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
    ENDPROC

    ! shell name: shell_002
    PROC shell_002( string strNoStepIn )
        ! <<< group name: grouped_faces_000 >>>
        ! ruled surface 001
        MoveL [[ 426.0, -1483.0, 1023.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-1, -1, -2, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ 426.0, -1483.0, 998.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-1, -1, -2, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ 426.0, -1483.0, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-1, -1, -2, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        ! ruled surface 003
        MoveL [[ 426.0, -1980.5, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-1, -1, -2, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ 426.0, -2478.0, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-1, -1, -2, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
    ENDPROC

    ! shell name: shell_000
    PROC shell_000( string strNoStepIn )
        ! <<< group name: grouped_faces_000 >>>
        ! ruled surface 001
        MoveL [[ -1484.0, -1483.0, 1023.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ -1484.0, -1483.0, 998.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ -1484.0, -1483.0, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        ! ruled surface 003
        MoveL [[ -1484.0, -1980.5, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
        MoveL [[ -1484.0, -2478.0, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez \Wobj:=cur_wobj;
    ENDPROC

    PROC run()
        ConfJ \Off;
        ConfL \Off;
        calib_x cnstNoStepIn;
        shell_002 cnstNoStepIn;
        shell_000 cnstNoStepIn;
        ConfJ \On;
        ConfL \On;
    ENDPROC

ENDMODULE
