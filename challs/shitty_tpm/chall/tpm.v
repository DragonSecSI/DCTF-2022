`timescale 1ns / 1ps

module TPM(clk, rst, data, lock);

input clk;
input rst;
input [7:0] data;
output lock;

reg [55:0] state;

initial state = 56'd0;
integer counter;
initial counter = 0;

assign lock = out == desired_value;

wire [55:0] key = 56'hdc35849333c6a8;

wire [55:0] out = rearranged ^ key;

wire [55:0] desired_value = 56'h781494ac201977;

always @(posedge clk) begin
    if (rst == 1'b1) begin
        state <= 56'b0;
        counter <= 0;
    end
    else begin
        if(counter < 8) begin
            state[(7 * counter)+: 7] <= data[6:0];
            counter <= counter + 1;
        end
    end
end

wire [55:0] rearranged;

assign rearranged = {
    state[21:13], 
    state[40:32], 
    state[52:50], 
    state[25:22], 
    state[42:41], 
    state[55:53], 
    state[4:0], 
    state[31:26], 
    state[49:43], 
    state[12:5]
};

endmodule
