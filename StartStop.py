import boto.ec2
import sys

# specify AWS keys
auth = {"aws_access_key_id": "AKIAJKYLZJYAN5BVIL4A", "aws_secret_access_key": "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"}
res=0
id1=''
def main():
    # read arguments from the command line and 
    # check whether at least two elements were entered
  
    if len(sys.argv) < 2:
        print "Usage: python EC2.py {start|stop}\n"
        sys.exit(0)
    else:
        action = sys.argv[1]
    
    ec2 = boto.ec2.connect_to_region("us-east-2", **auth)
    reservations = ec2.get_all_instances()
    print reservations
    for res in reservations:
        for inst in res.instances:
            id1 = inst.id
            print "id1", id1
            if action == "start" and (inst.state == "stopped" or inst.state == "stopping"):
                startInstance(id1,ec2)
            elif action == "stop"and inst.state == "running":
                stopInstance(id1,ec2)
            else:
                print "Usage: python EC2.py {start|stop}\n"


def startInstance(id1,ec2):
    print "Starting the instance..."

    #ec2 = boto.ec2.connect_to_region("us-east-2", **auth)
    # change instance ID appropriately  
    try:
    
        ec2.start_instances(instance_ids = id1)
        
    except Exception, e2:
        error1 = "Error1: %s" % str(e2)
        print(error1)
        sys.exit(0)

def stopInstance(id1,ec2):
    print "Stopping the instance..."
    #ec2 = boto.ec2.connect_to_region("us-east-2", **auth)

    try:
        print "inst.id" , id1
        ec2.stop_instances(instance_ids = id1)

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

if __name__ == '__main__':
    main()
    
