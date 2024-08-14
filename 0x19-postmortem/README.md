### Postmortem : Web Application Outage

---

#### **Issue Summary**

**Duration of Outage:**  
Start Time: 2024-08-14, 10:00 AM UTC  
End Time: 2024-08-14, 11:30 AM UTC  

**Impact:**  
The outage affected the main web application, causing significant slowdowns and periods of unavailability. Approximately 75% of users experienced delays in page load times exceeding 10 seconds, while 30% of users faced complete service interruptions.

**Root Cause:**  
The issue was traced back to a misconfigured load balancer that resulted in uneven traffic distribution, overloading a subset of application servers.

---

#### **Timeline**

- **10:05 AM UTC:** Monitoring alert triggered, indicating increased response times for the web application.
- **10:10 AM UTC:** Engineers began investigating the application servers, suspecting a database performance issue.
- **10:25 AM UTC:** Investigation into database performance showed normal operation; focus shifted to the network layer.
- **10:35 AM UTC:** Traffic logs revealed that one server was receiving 80% of the total traffic, while others were idle.
- **10:45 AM UTC:** The load balancer configuration was identified as the potential root cause; escalated to the network team.
- **11:00 AM UTC:** Network team confirmed a recent configuration change on the load balancer.
- **11:15 AM UTC:** Load balancer configuration was rolled back to the previous version.
- **11:30 AM UTC:** Service was fully restored, and monitoring showed normal traffic distribution and response times.

---

#### **Root Cause and Resolution**

**Root Cause:**  
The load balancer configuration was modified during a routine update. An incorrect parameter in the configuration led to uneven traffic distribution, overwhelming one server while leaving others underutilized. The misconfiguration caused the overloaded server to struggle with the traffic, leading to slow response times and, in some cases, complete timeouts.

**Resolution:**  
Once the root cause was identified, the configuration was rolled back to the previous, stable version. This immediately redistributed traffic evenly across all servers, restoring normal service. Monitoring tools confirmed the fix as response times normalized, and no further issues were detected post-resolution.

---

#### **Corrective and Preventative Measures**

**Improvements:**  
- **Configuration Review Process:** Implement a more rigorous review process for configuration changes to critical components like load balancers.
- **Load Testing:** Regular load testing to ensure that any configuration changes do not negatively impact traffic distribution.
- **Enhanced Monitoring:** Add specific alerts for unusual traffic patterns on individual servers to catch similar issues more quickly.

**Tasks:**
- **Patch Load Balancer:** Ensure that the latest load balancer software patches are applied to prevent similar configuration issues.
- **Update Documentation:** Revise the documentation to include detailed steps for configuring the load balancer, highlighting the critical parameters.
- **Add Traffic Monitoring:** Implement monitoring for load distribution across servers to detect and alert on uneven traffic distribution in real time
