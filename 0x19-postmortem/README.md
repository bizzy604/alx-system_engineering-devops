---

### **Postmortem: When Our Web App Decided to Take a Nap**

---

#### **Issue Summary**

**Duration of Outage:**  
Start Time: 2024-08-14, 10:00 AM UTC  
End Time: 2024-08-14, 11:30 AM UTC  

**Impact:**  
For an hour and a half, our web application felt like it was trying to load through molasses. Users experienced page load times slower than a snail’s pace, with about 75% of users wondering if their internet was broken. Meanwhile, 30% of our users faced the dreaded spinning wheel of doom.

**Root Cause:**  
Turns out, our load balancer had a bit of a breakdown and decided to make one server do all the work while the others sat back with their feet up.

---

#### **Timeline**

- **10:05 AM UTC:** “Houston, we have a problem!” Our monitoring system pinged us with skyrocketing response times.
- **10:10 AM UTC:** Like good detectives, we first checked out the usual suspect: the database. But it was innocent and as smooth as ever.
- **10:25 AM UTC:** With the database cleared, we switched gears and looked into the network layer – where things got interesting.
- **10:35 AM UTC:** Bingo! We found one server buckling under the weight of 80% of the traffic, while the others were barely breaking a sweat.
- **10:45 AM UTC:** Suspicions pointed to the load balancer, so we called in the network team to take a closer look.
- **11:00 AM UTC:** The network team confirmed our hunch – a recent config change had gone rogue.
- **11:15 AM UTC:** We rolled back the load balancer configuration, restoring balance to the force (and our traffic).
- **11:30 AM UTC:** All systems were go, with traffic flowing smoothly across all servers again.

---

#### **Root Cause and Resolution**

**Root Cause:**  
Our load balancer, bless its heart, got a bit confused during a routine update. A misconfigured parameter led it to believe that one server was Hercules, capable of handling almost all the traffic alone. Unfortunately, that server wasn’t quite up to the task, and things started to slow down…a lot.

**Resolution:**  
We gently reminded our load balancer that sharing is caring by rolling back to the previous configuration. This instantly spread the traffic love across all servers, and the web app was back to running at full speed in no time.

---

#### **Corrective and Preventative Measures**

**Improvements:**  
- **Configuration Review Process:** Before making any changes, we’ll double-check (and triple-check) our load balancer settings to avoid any more hero servers.
- **Load Testing:** We’ll make sure to regularly stress-test our servers to catch any potential issues before they spiral out of control.
- **Enhanced Monitoring:** We’re adding alerts for uneven traffic distribution so that we can catch these issues even faster next time.

**Tasks:**
- **Patch Load Balancer:** We’ll apply the latest software patches to the load balancer to keep it in top shape.
- **Update Documentation:** Our team will revise the load balancer configuration guide, complete with big red warnings around the critical settings.
- **Add Traffic Monitoring:** We’ll set up real-time traffic monitoring across all servers to prevent another lone-server meltdown.

---

### **Diagram Concept:**

**Before the Fix:**
- Imagine a diagram where most of the traffic arrows are heading to a single, overworked server. This server could be shown sweating, with a distressed face or with exaggerated "cracks" under the load.

**After the Fix:**
- Show traffic evenly distributed across all servers. Each server could be illustrated as content and balanced, with even the previously overworked server looking relieved.

---

