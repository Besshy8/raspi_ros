package main
//go:generate gengo msg std_msgs/String
import (
"fmt"
"github.com/akio/rosgo/ros"
"os"
"std_msgs"
"time"
)
func main() {
 node, _ := ros.NewNode("/talker", os.Args)
 defer node.Shutdown()
 pub, _ := node.NewPublisher("/chatter", std_msgs.MsgString)
 for node.OK() {
 node.SpinOnce()
 var msg std_msgs.String
 msg.Data = fmt.Sprintf("hello %s", time.Now().String())
 pub.Publish(&msg)
 time.Sleep(time.Second)
 }
}
