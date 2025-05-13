
# **Google Cloud: VPC Network and Subnet Creation Using `gcloud` CLI**

## **Introduction**
Virtual Private Cloud (VPC) is a fundamental component of Google Cloud, providing a private network within Google’s global infrastructure. It allows users to define a network topology, configure IP address ranges, subnets, and manage routing policies. Google Cloud offers two types of subnet modes for VPC: **automatic** and **custom**. In this tutorial, we focus on the process of creating a custom VPC network and configuring subnets within it using the `gcloud` CLI.

## **Prerequisites**
Before proceeding with the configuration, ensure that you have:
1. A valid Google Cloud account.
2. A project set up within Google Cloud.
3. The Google Cloud SDK (`gcloud CLI`) installed on your local machine or access to **Google Cloud Shell**.
4. Proper permissions to create resources such as networks and subnets.

## **Theory: Custom VPC and Subnet Configuration**

### **Virtual Private Cloud (VPC)**
A **VPC** is a global resource that enables users to provision and manage private networks in Google Cloud. It provides:
- **Isolation** from other networks in Google Cloud.
- **Security** through private IP address ranges, firewalls, and VPNs.
- **Routing** that can be customized for specific needs.

A **custom mode VPC** provides the flexibility to create custom subnets for each region, giving more control over IP address allocation and network configuration.

### **Subnets in VPC**
A **subnet** is a range of IP addresses within a VPC network, assigned to specific regions. Subnets can be either in **automatic mode** (Google Cloud automatically creates subnets for each region) or **custom mode** (you manually create subnets with specific IP ranges).

The key difference between the two modes is that in **custom mode**, you define the exact size and range of each subnet. This allows for more fine-tuned control, especially useful in large, distributed systems.

## **Step-by-Step Guide: Creating a VPC and Subnet in Google Cloud**

### **Step 1: Set Up Authentication and Configuration**

1. **Authenticate your Google Cloud account:**
   To begin interacting with Google Cloud resources, you must first authenticate your account. Use the following command to ensure that you are authenticated:
   ```bash
   gcloud auth login
   ```

2. **Set your active project:**
   Ensure that your desired project is set as active by running:
   ```bash
   gcloud config set project <YOUR_PROJECT_ID>
   ```

3. **Verify authentication and project configuration:**
   ```bash
   gcloud auth list
   gcloud config list project
   ```
   This ensures that your authentication credentials and project configurations are correctly set.

### **Step 2: Create a Custom VPC Network**

A custom VPC provides flexibility in defining subnets for specific regions. To create a custom VPC network, execute the following command:
```bash
gcloud compute networks create labnet --subnet-mode=custom
```
- `labnet`: The name of the VPC network.
- `--subnet-mode=custom`: This flag defines the network as custom mode, allowing for the creation of user-defined subnets.

**Output Example:**
```
NAME: labnet
SUBNET_MODE: CUSTOM
BGP_ROUTING_MODE: REGIONAL
```

### **Step 3: Create a Subnet within the VPC Network**

Next, we create a subnet within the custom VPC. This subnet will be located in the **us-central1** region and will have a custom IP range (`10.0.0.0/28`), which defines the address space for resources within the subnet.

```bash
gcloud compute networks subnets create labnet-sub    --network labnet    --region us-central1    --range 10.0.0.0/28
```
- `labnet-sub`: The name of the subnet being created.
- `--network labnet`: Specifies the custom VPC network in which the subnet will reside.
- `--region us-central1`: Defines the region for the subnet.
- `--range 10.0.0.0/28`: The IP address range allocated to the subnet. The `/28` subnet mask allows for 16 IP addresses, of which 14 are usable for hosts.

**Output Example:**
```
Created subnet [labnet-sub] in region [us-central1] with range [10.0.0.0/28].
```

### **Step 4: View the Created Networks**

To verify that your VPC network has been successfully created, use the following command to list all networks:
```bash
gcloud compute networks list
```

**Output Example:**
```
NAME      SUBNET_MODE  BGP_ROUTING_MODE  ANCESTRY
default   AUTO         REGIONAL          /
labnet    CUSTOM       REGIONAL          /
```
Here, `labnet` is the custom VPC network you created.

### **Step 5: List Subnets in the Network**

After creating the subnet, you can list the subnets under the `labnet` network by using:
```bash
gcloud compute networks subnets list --network=labnet
```

**Output Example:**
```
NAME         REGION         NETWORK  RANGE
labnet-sub   us-central1    labnet   10.0.0.0/28
```

### **Step 6: Clean Up (Optional)**

To delete the VPC and subnet you created (for cleanup purposes), use the following commands:

1. **Delete the subnet:**
   ```bash
   gcloud compute networks subnets delete labnet-sub --region=us-central1
   ```

2. **Delete the network:**
   ```bash
   gcloud compute networks delete labnet
   ```

---

## **Conclusion**

In this tutorial, we have successfully created a custom VPC network and subnet in Google Cloud using the `gcloud` CLI. This process is crucial for managing network configurations in cloud environments, providing fine-grained control over IP address allocation and regional network organization. By using the `gcloud` CLI, we can automate and streamline network management in Google Cloud, which is especially useful for large-scale deployments.

This process is foundational for various Google Cloud services, including compute instances, load balancers, and more, and it lays the groundwork for more advanced networking configurations such as VPNs, peering, and firewalls.

--- 

