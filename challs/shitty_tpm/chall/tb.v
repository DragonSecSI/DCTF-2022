`timescale 1ns / 1ps

module tb(   );

reg clk;
reg rst;

reg [7:0] data;

wire lock;

TPM tpm(clk, rst, data, lock);

initial begin
    clk = 0;
    rst = 1;

    #5;

    clk = 1;
    #5;
    clk = 0;
    #5;
    rst = 0;
    data = 8'h78;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h37;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h24;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h61;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h49;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h50;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h3e;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    data = 8'h75;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    clk = 1;
    #5;
    clk = 0;
    #5;
    clk = 1;
    #5;
    clk = 0;

    $display("%d", lock);


    //pass = x7$aIP>u    78 37 24 61 49 50 3e 75



end


endmodule
