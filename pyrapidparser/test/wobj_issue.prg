MODULE ODC
    PERS tooldata hotwirez := [ TRUE, [ [ 0.000, 0.000, 733.000 ], [ 1.000000000, 0.000000000, 0.000000000, 0.000000000 ] ], [ 10.0, [ 0.040, 0.000, 733.000 ], [ 1, 0, 0, 0 ], 0, 0, 0 ] ];
    PERS pos Pos_Offset := [ 0, 0, 0 ];
    PERS speeddata cur_vel := [ 200.0, 200.0, 1000.0, 1000.0 ];
    PERS zonedata cur_zone := [FALSE, 1, 1, 50, 0.1, 50, 0.1];
    !PERS wobjdata cur_wobj := [ FALSE, TRUE, "", [ [ -0.000, -0.000, -1400.000 ], [ 1.000000000, 0.000000000, 0.000000000, 0.000000000 ] ], [ [0, 0, 0], [1, 0, 0 ,0] ] ];

    PERS string cnstNoStepIn := "ohno";

    ! shell name: shell_000
    PROC shell_000( string strNoStepIn )
        ! <<< group name: grouped_faces_000 >>>
        ! ruled surface 001
        MoveL [[ -1484.0, -1483.0, 973.0 ],[ 0.011458, 0.707014, -0.707014, 0.011458 ],[-2, 0, -3, 0],[ 9E+09,9E+09,9E+09,9E+09,9E+09,9E+09 ]],cur_vel, cur_zone, hotwirez;
        ! ruled surface 003
    ENDPROC

    PROC run()
        ConfJ \Off;
        ConfL \Off;
        shell_000 cnstNoStepIn;
        ConfJ \On;
        ConfL \On;
    ENDPROC

    PROC main()
        ! run the toolpath
        run;
    ENDPROC


ENDMODULE