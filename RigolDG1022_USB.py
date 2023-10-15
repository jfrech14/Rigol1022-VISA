import time
import pyvisa

def RigolDG1022_Connect():
    DeviceList=pyvisa.ResourceManager().list_resources()
    match='DG'
    for dev in DeviceList:
        if match in dev:
            Rigol1=dev

    instRigol1=pyvisa.ResourceManager().open_resource(Rigol1)
    DeviceName=instRigol1.query('*IDN?')
    print("Connected to: "+ DeviceName[0:18] +' '+ DeviceName[19:26] + ' on '+Rigol1)
    return instRigol1

def RigolDG1022_Stop(inst):
    wait=.0001
    inst.write(':OUTP ' + 'OFF')
    time.sleep(wait)
    inst.write(':OUTP:CH2 ' + 'OFF')
    time.sleep(wait)

def RigolDG1022_Init(inst,Ch,State,Pol,VHigh,VLow,Width,Duty,BurstState, TrigSource, TrigSlope):
    wait=.0001
    if Ch==1:
        inst.write(':OUTP ' + State)
        time.sleep(wait)
        inst.write(':OUTP:POL ' + Pol)
        time.sleep(wait)
        inst.write(':VOLT:HIGH ' + str(VHigh))
        time.sleep(wait)
        inst.write(':VOLT:LOW ' + str(VLow))
        time.sleep(wait)
        inst.write(':FUNC ' + 'PULS')
        time.sleep(wait)
        inst.write(':PULS:DCYC ' + str(Duty))
        time.sleep(wait)
        inst.write(':PULS:PER ' + str(Width*2))
        time.sleep(wait)
        inst.write(':BURS:STAT ' + BurstState)
        time.sleep(wait)
        inst.write(':BURS:MODE ' + 'TRIG')
        time.sleep(wait)
        inst.write(':BURS:NCYC ' + '1')
        time.sleep(wait)
        inst.write(':TRIG:SOUR ' + TrigSource)
        time.sleep(wait)
        inst.write(':TRIG:SLOP ' + TrigSlope)
        time.sleep(wait)
        inst.write(':TRIG:DEL ' + str(0))
        time.sleep(wait)
    elif Ch==2:
        inst.write(':OUTP:CH2 ' + State)
        time.sleep(wait)
        inst.write(':OUTP:POL:CH2 ' + Pol)
        time.sleep(wait)
        inst.write(':VOLT:HIGH:CH2 ' + str(VHigh))
        time.sleep(wait)
        inst.write(':VOLT:LOW:CH2 ' + str(VLow))
        time.sleep(wait)
        inst.write(':FUNC:CH2 ' + 'PULS')
        time.sleep(wait)
        inst.write(':PULS:DCYC:CH2 ' + str(Duty))
        time.sleep(wait)
        inst.write(':PULS:PER:CH2 ' + str(Width*2))
        time.sleep(wait)
    else:
        None

def RigolDG1022_Output(inst,Ch,State,Pol):
    wait=.0001
    if Ch==1:
        inst.write(':OUTP ' + State)
        time.sleep(wait)
        inst.write(':OUTP:POL ' + Pol)
    elif Ch==2:
        inst.write(':OUTP:CH2 ' + State)
        time.sleep(wait)
        inst.write(':OUTP:POL:CH2 ' + Pol)
    else:
        None

def RigolDG1022_Voltage(inst,Ch,VHigh,VLow):
    wait=.0001
    if Ch==1:
        inst.write(':VOLT:HIGH ' + str(VHigh))
        time.sleep(wait)
        inst.write(':VOLT:LOW ' + str(VLow))
        time.sleep(wait)
    elif Ch==2:
        inst.write(':VOLT:HIGH:CH2 ' + str(VHigh))
        time.sleep(wait)
        inst.write(':VOLT:LOW:CH2 ' + str(VLow))
        time.sleep(wait)
    else:
        None
        
def RigolDG1022_Pulse(inst,Ch,Width,Duty):
    wait=.0001
    if Ch==1:
        inst.write(':FUNC ' + 'PULS')
        time.sleep(wait)
        inst.write(':PULS:DCYC ' + str(Duty))
        time.sleep(wait)
        inst.write(':PULS:PER ' + str(Width*2))
        time.sleep(wait)
    elif Ch==2:
        inst.write(':FUNC:CH2 ' + 'PULS')
        time.sleep(wait)
        inst.write(':PULS:DCYC:CH2 ' + str(Duty))
        time.sleep(wait)
        inst.write(':PULS:PER:CH2 ' + str(Width*2))
        time.sleep(wait)
    else:
        None

def RigolDG1022_Ch1TriggeredBurst(inst,BurstState):
    wait=.0001
    inst.write(':BURS:STAT ' + BurstState)
    time.sleep(wait)
    inst.write(':BURS:MODE ' + 'TRIG')
    time.sleep(wait)
    inst.write(':BURS:NCYC ' + '1')
    time.sleep(wait)
    inst.write(':BURS:GATE:POL'+ 'NORM')
    time.sleep(wait)
    inst.write(':BURS:PHAS'+ '0.0')
    time.sleep(wait)

def RigolDG1022_Ch1Trigger(inst,TrigSource,TrigSlope):
    wait=.0001
    inst.write(':TRIG:SOUR ' + TrigSource)
    time.sleep(wait)
    inst.write(':TRIG:SLOP ' + TrigSlope)
    time.sleep(wait)
    inst.write(':TRIG:DEL ' + str(0.0))
    time.sleep(wait)
