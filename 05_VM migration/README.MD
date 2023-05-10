# Migrate Your Existing OnPremise Workloads to Amazon EC2

Using `VM Import` migrate your existing VM-based applications and preserve the software and settings that you have configured in your existing VM.

# Migrate Your Existing On-Premise Workloads to Amazon EC2

This guide provides step-by-step instructions on how to migrate your existing on-premise virtual machine (VM) workloads to Amazon EC2 using the VM Import feature. By following these steps, you will be able to preserve the software and settings configured in your current VM. Let's enhance your README by organizing the content and adding some formatting.

## Prerequisites

Before you begin the migration process, make sure you have the following:

- On-premise VM (preferably in VMWare / Virtualbox)
  - If you have a `*.vmdk` image of your VM, that will also suffice.
  - **MUST**: You should have the username and password to log into this VM.
- AWS CLI with access to Administrator privileges.
  - You can adjust the privileges based on your specific requirements.

## Steps to Migrate Your VM to Amazon EC2

1. **Export VM & Upload to S3**

   Depending on your virtualization tool, follow the appropriate procedure to export your VM into a `*.vmdk` or `*.ova` image. Upload the image to an S3 bucket and take note of the `bucket_name` and `vm_image_name`.

2. **Global Customization Variables**

   Set the global variables for the bucket name and VM image name in your preferred scripting language (e.g., shell script).

   ```sh
   bucket_name="n-backup"
   vm_image_name="VM-Import/vCentOS7-disk002.vmdk"
   ```

3. **Create Trust Policy**

   Create the IAM trust policy JSON file named `trust-policy.json` with the following content:

   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
         {
            "Effect": "Allow",
            "Principal": { "Service": "vmie.amazonaws.com" },
            "Action": "sts:AssumeRole",
            "Condition": {
               "StringEquals": {
                  "sts:Externalid": "vmimport"
               }
            }
         }
      ]
   }
   ```

4. **Create the IAM Role for VM Import**

   Create the IAM role named `vmimport` using the trust policy created in the previous step:

   ```sh
   aws iam create-role --role-name vmimport --assume-role-policy-document "file://trust-policy.json"
   ```

5. **Create the IAM Policy (role-policy.json)**

   Create the IAM policy that will be attached to the `vmimport` role. The bucket name is obtained from the global variable:

   ```sh
   echo '{
      "Version":"2012-10-17",
      "Statement":[
         {
            "Effect":"Allow",
            "Action":[
               "s3:GetBucketLocation",
               "s3:GetObject",
               "s3:ListBucket" 
            ],
            "Resource":[
               "arn:aws:s3:::'${bucket_name}'",
               "arn:aws:s3:::'${bucket_name}'/*"
            ]
         },
         {
            "Effect":"Allow",
            "Action":[
               "ec2:ModifySnapshotAttribute",
               "ec2:CopySnapshot",
               "ec2:RegisterImage",
               "ec2:Describe*"
            ],
            "Resource":"*"
         }
      ]
   }
   ' | sudo tee role-policy.json
   ```

6. **Attach the Policy to IAM Role `vmimport`**

Attach the IAM policy to the `vmimport` role using the following command:

```sh
aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document "file://role-policy.json"
```

7. **Begin VM Image Import Task**

   Start the import of the VM image by executing the following commands:

   ```sh
   # Set the metadata
   echo '[
     {
       "Description": "centosv7",
       "Format": "vmdk",
       "UserBucket": {
           "S3Bucket": "'${bucket_name}'",
           "S3Key": "'${vm_image_name}'"
       }
   }]
   ' > containers.json
   ```

   ```sh
   aws ec2 import-image --description "centosv7" --disk-containers "file://containers.json"
   ```

   After running the command, you will receive output similar to the following:

   ```sh
   {
       "Description": "centosv7",
       "ImportTaskId": "import-ami-0d6db3a35d431e4e3",
       "Progress": "2",
       "SnapshotDetails": [
           {
               "DiskImageSize": 0.0,
               "Format": "VMDK",
               "UserBucket": {
                   "S3Bucket": "n-backup",
                   "S3Key": "VM-Import/vCentOS7-disk002.vmdk"
               }
           }
       ],
       "Status": "active",
       "StatusMessage": "pending"
   }
   ```

   Make note of the `ImportTaskId` as you will need it to check the progress of the import job.

8. **Check the Status of VM Import Jobs**

   To check the status of the VM import task, use the following command:

   ```sh
   aws ec2 describe-import-image-tasks --import-task-ids "import-ami-0d6db3a35d431e4e3"
   ```

9. **Check VM Import Progress**

   To check the progress of the VM import, execute the following command:

   ```sh
   aws ec2 describe-import-image-tasks --import-task-ids "import-ami-0d6db3a35d431e4e3"
   ```

   You will receive output similar to the following:

   ```sh
   {
       "ImportImageTasks": [
           {
               "Description": "centosv7",
               "ImportTaskId": "import-ami-0d6db3a35d431e4e3",
               "Progress": "30",
               "SnapshotDetails": [
                   {
                       "Description": "centosv7",
                       "DiskImageSize": 931182592.0,
                       "Format": "VMDK",
                       "Status": "completed",
                       "UserBucket": {
                           "S3Bucket": "n-backup",
                           "S3Key": "VM-Import/vCentOS7-disk002.vmdk"
                       }
                   }
               ],
               "Status": "active",
               "StatusMessage": "updating"
           }
       ]
   }
   ```

10. **Completion Status**

    To retrieve the completion status of the VM import, run the following command:

    ```sh
    aws ec2 describe-import-image-tasks --import-task-ids "import-ami-0d6db3a35d431e4e3"
    ```

    The output will contain the details of the imported VM, including the `ImageId`, `SnapshotId`, and other relevant information.

11. **Launch a New EC2
                           --
To launch a new EC2 instance from the imported VM image, follow these steps:

1. Retrieve the `ImageId` from the completion status output of the VM import task.

2. Launch a new EC2 instance using the `run-instances` command with the `ImageId` and other desired parameters. For example:

   ```sh
   aws ec2 run-instances --image-id <ImageId> --instance-type <InstanceType> --key-name <KeyName> --subnet-id <SubnetId> --security-group-ids <SecurityGroupIds> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyInstance}]'
   ```

   Replace `<ImageId>` with the actual ImageId obtained from the completion status output. Set the `<InstanceType>` to the desired EC2 instance type, `<KeyName>` to the name of your key pair, `<SubnetId>` to the ID of the subnet where the instance will be launched, and `<SecurityGroupIds>` to the IDs of the security groups for the instance.

   You can also specify additional parameters as needed, such as IAM instance profile, user data, etc.

3. Once the EC2 instance is launched, you can connect to it using SSH or other remote access methods, using the appropriate username and password you had in the on-premise VM.

That's it! You have successfully migrated your on-premise VM to Amazon EC2 and launched a new instance from the imported image. Remember to review and adjust the instance configuration, networking, and security settings based on your specific requirements.

##### References

1. [AWS CLI - import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html)

2. [AWS Blogs - Importing a VM](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#import-vm)

3. Inspired from (https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=category%23migration&awsf.getting-started-content-type=*all)
