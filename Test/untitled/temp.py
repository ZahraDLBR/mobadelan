def test_var_args_call(arg1, ar, arg3):
    print("arg1:", arg1)
    print ("arg2:", ar)
    print ("arg3:", arg3)

kwargs = {"arg3": 3, "arhjjklzzzzzzzzzzz": "two"}
test_var_args_call(1, *kwargs)