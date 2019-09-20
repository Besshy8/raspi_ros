package main

//go:generate gengo msg raspi_ros/GoTwist
//go:generate gengo msg raspi_ros/MotorFreq
//go:generate gengo srv std_srvs/Trigger
//go:generate gengo msg std_msgs/Empty
import "github.com/akio/rosgo/ros"
import "os"
import "fmt"
//import "geometry_msgs"
import "math"
import "log"
import "raspi_ros"
import "strconv"
import "std_srvs"
import "std_msgs"
//import "time"

// 	use topic for motor enpower

func msgCallBackOn(emp *std_msgs.Empty){
	fmt.Println("--------------------")
	fmt.Println("Called msgCallBackOn")

	fileOn, errOn := os.OpenFile("/dev/rtmotoren0",os.O_WRONLY,0666)
	
	if errOn != nil {
		log.Fatal(errOn)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOn.Close()
	fileOn.WriteString("1\n")

	// for Debag

	fileOnTxt, errOnTxt := os.OpenFile("/home/ubuntu/text/file2.txt",os.O_WRONLY,0666)
	
	if errOnTxt != nil {
		log.Fatal(errOnTxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOnTxt.Close()
	fileOnTxt.WriteString("1\n")

	fmt.Println("MOTOR ON")	
	
}

func msgCallBackOff(emp *std_msgs.Empty){
	fmt.Println("--------------------")
	fmt.Println("Called msgCallBackOff")

	fileOn, errOn := os.OpenFile("/dev/rtmotoren0",os.O_WRONLY,0666)
	
	if errOn != nil {
		log.Fatal(errOn)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOn.Close()
	fileOn.WriteString("0\n")

	// for Debag

	fileOnTxt, errOnTxt := os.OpenFile("/home/ubuntu/text/file2.txt",os.O_WRONLY,0666)
	
	if errOnTxt != nil {
		log.Fatal(errOnTxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOnTxt.Close()
	fileOnTxt.WriteString("0\n")

	fmt.Println("MOTOR OFF")
}

// use service for motor enpower

func srvCallbackOn(srv *std_srvs.Trigger) std_srvs.TriggerResponse {
	fmt.Println("--------------------")
	fmt.Println("Called srvCallbackOn() func")

	fileOn, errOn := os.OpenFile("/dev/rtmotoren0",os.O_WRONLY,0666)
	
	if errOn != nil {
		log.Fatal(errOn)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOn.Close()
	fileOn.WriteString("1\n")

	// for Debag
	fileOnTxt, errOnTxt := os.OpenFile("/home/ubuntu/text/file.txt",os.O_WRONLY,0666)
	
	if errOnTxt != nil {
		log.Fatal(errOnTxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOnTxt.Close()
	fileOnTxt.WriteString("1\n")

	var res std_srvs.TriggerResponse

	res.Success = true
	res.Message = "motor_on"

	return res

}

func srvCallbackOff(srv *std_srvs.Trigger) std_srvs.TriggerResponse{
	fmt.Println("--------------------")
	fmt.Println("Called srvCallbackOff() func")

	fileOn, errOn := os.OpenFile("/dev/rtmotoren0",os.O_WRONLY,0666)
	
	if errOn != nil {
		log.Fatal(errOn)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOn.Close()
	fileOn.WriteString("0\n")

	// for Debag
	fileOnTxt, errOnTxt := os.OpenFile("/home/ubuntu/text/file.txt",os.O_WRONLY,0666)
	
	if errOnTxt != nil {
		log.Fatal(errOnTxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileOnTxt.Close()
	fileOnTxt.WriteString("0\n")

	var res std_srvs.TriggerResponse

	res.Success = true
	res.Message = "motor_off"

	return res

}

// subscribe frequency for motor

func callBackFreq(msg *raspi_ros.MotorFreq){
	left_Freq := msg.WheelLeft
	right_Freq := msg.WheelRight
	fileLeft, errLeft := os.OpenFile("/dev/rtmotor_raw_l0",os.O_WRONLY,0666)

	fmt.Println(left_Freq,right_Freq)
	
	if errLeft != nil {
		log.Fatal(errLeft)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileLeft.Close()
	fileLeft.WriteString(strconv.Itoa(int(left_Freq)))

	fileRight, errRight := os.OpenFile("/dev/rtmotor_raw_r0",os.O_WRONLY,0666)
	if errRight != nil {
		log.Fatal(errRight)
		fmt.Println("ERROR FILE OPEN")
	}
	defer fileRight.Close()
	fileLeft.WriteString(strconv.Itoa(int(right_Freq)))

	// for Debag
	
	filetxt, errtxt := os.OpenFile("/home/ubuntu/text/file.txt",os.O_WRONLY,0666)
	
	if errtxt != nil {
		log.Fatal(errtxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer filetxt.Close()
	filetxt.WriteString(strconv.Itoa(int(left_Freq)))
	

}

// subscribe velocity for motor

func callBackCmdvel(msg *raspi_ros.GoTwist){
	vel_x := msg.LinearX
	rot_z := msg.AngularZ
	r := 0.0225
	left_Freq :=  (400 / (2*math.Pi*r))*vel_x - (400 / math.Pi)*rot_z
	right_Freq := (400 / (2*math.Pi*r))*vel_x + (400 / math.Pi)*rot_z
	left_Freq = math.Floor(left_Freq)
	right_Freq = math.Floor(right_Freq)
	fmt.Println(left_Freq)

	// left wheel
	fileLeft, errLeft := os.OpenFile("/dev/rtmotor_raw_l0",os.O_WRONLY,0666)
	if errLeft != nil {
		log.Fatal(errLeft)
	}
	defer fileLeft.Close()
	
	if left_Freq == 0 {
		fileLeft.WriteString("0.00")	
	} else if left_Freq == 353 {
		fileLeft.WriteString("+353")
	} else if left_Freq == 200 {
		fileLeft.WriteString("+200")
	} else {
		fileLeft.WriteString(strconv.Itoa(int(left_Freq)))	
	}

	//right wheel
	
	fileRight, errRight := os.OpenFile("/dev/rtmotor_raw_r0",os.O_WRONLY,0666)
	if errRight != nil {
		log.Fatal(errRight)
	}
	defer fileRight.Close()
	if right_Freq == 0 {
		fileRight.WriteString("0.00")	
	}else if right_Freq == 353 {
		fileRight.WriteString("+353")
	} else if right_Freq == 200 {
		fileRight.WriteString("+200")
	} else {
		fileRight.WriteString(strconv.Itoa(int(right_Freq)))	
	}
	// for Debag left
	
	filetxt, errtxt := os.OpenFile("/home/ubuntu/text/file.txt",os.O_WRONLY,0666)
	
	if errtxt != nil {
		log.Fatal(errtxt)
		fmt.Println("ERROR FILE OPEN")
	}
	defer filetxt.Close()
	if left_Freq == 0 {
		filetxt.WriteString("0.00")	
	} else if left_Freq == 200 {
		filetxt.WriteString("+200")
	}else if left_Freq == 353 {
		filetxt.WriteString("+353")
	}  else {
		filetxt.WriteString(strconv.Itoa(int(left_Freq)))	
	}
	
	// for Debag right
	
	filetxtR, errtxtR := os.OpenFile("/home/ubuntu/text/file.txt",os.O_WRONLY,0666)
	
	if errtxtR != nil {
		log.Fatal(errtxtR)
		fmt.Println("ERROR FILE OPEN")
	}
	defer filetxtR.Close()
	
	if right_Freq == 0 {
		filetxtR.WriteString("0.00")	
	} else if right_Freq == 200 {
		filetxtR.WriteString("+200")
	}else if right_Freq == 353 {
		filetxtR.WriteString("+353")
	}  else {
		filetxtR.WriteString(strconv.Itoa(int(right_Freq)))	
	}
	
	//filetxt.WriteString(strconv.Itoa(int(right_Freq)))
}




func main()  {
	node, err := ros.NewNode("Motor",os.Args)
	fmt.Println("Node Start")
	if err != nil{
		fmt.Println(err)
		os.Exit(-1)
	}
	defer node.Shutdown()
	node.NewSubscriber("/GoCmdvel",raspi_ros.MsgGoTwist,callBackCmdvel)
	node.NewSubscriber("/motorFreq",raspi_ros.MsgMotorFreq,callBackFreq)
	node.NewSubscriber("motor_on_ByMSG",std_msgs.MsgEmpty,msgCallBackOn)
	node.NewSubscriber("motor_off_ByMSG",std_msgs.MsgEmpty,msgCallBackOff)
	
	srv_on := node.NewServiceServer("motor_on",std_srvs.SrvTrigger,srvCallbackOn)
	if srv_on == nil {
		fmt.Println("Failed to initialize '/motor_on' service server")
		os.Exit(-1)
	}
	defer srv_on.Shutdown()

	srv_off := node.NewServiceServer("motor_off",std_srvs.SrvTrigger,srvCallbackOff)
	if srv_off == nil {
		fmt.Println("Failed to initialize '/motor_off' service server")
		os.Exit(-1)
	}
	defer srv_off.Shutdown()

	for node.OK(){
		node.SpinOnce()
	}
	fmt.Println("Stop Node")
}
