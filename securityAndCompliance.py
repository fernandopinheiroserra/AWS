
def securityResponsabilities():
    sharedResponsabilityModel = []
    sharedResponsabilityModel = ['Security of cloud computing infraestructures an data is a shared responsability between the custumer and AWS', 'the customer has some components to worry about']
    awsResponsability = securityOfTheCLoud
    customerResponsability = securityInTheCloud
    securityOfTheCLoud = ['AWS is responsible for Protecting the Infraestructure: Physical security of data centers hosting the AWS Cloud', 'Security of Software, networking an every component that runs the cloud computing services']
    securityInTheCloud = ['Customer is responsible for varying levels of security functions, depending on the AWS Cloud used', 'Protecting customer data and data encryption', 'Identify and access Management', 'Patching Opeating Systems of VMs', 'Configuring Firewalls']

def wellArchitectureInfraestructure():
    fivePillars = ['Operational Excellence', 'Security', 'Reliability', 'Performance Efficiency', 'Cost optmization']

def securityPillar():
    features = [f"Identify and Access Management({iam})", detectiveControls, infraestructureProtection, dataProtection, incidentResponse]
    iam = ['Actively manage all-user access', 'Use strong identity foundation', 'principle of last privilege']
    detectiveControls = ['Enable traceability: Who did what, when?', 'Actively Monitor Alerts', 'Audit actions an changes to environment in real time']
    infraestructureProtection = ['apply sercurity to all layers of infraestructure (not just the outer layer)', 'Virtual servers: secure multiple layers like subnet, load balancer and OS', 'Security best pratices should be automated to save time and money when scaling']
    whenProtectData = ['At Rest: Image save in S3 bucket', 'In transit: Email being send from one server to another']
    dataProtection = ['Security Mechanisms should be adjusted depending on the sensitivity of the data', 'Keep people away from data']
    incidentResponse = ['intervene, investigate and deal with all security events', 'Once issue is resolved, update incidente management process', 'continue to learn from past mistakes and security events']
    return iam

def principleOfLeastPrivilege():
    concept = 'Provide access only to the resources that a person need to do his job, no more, no less'
    features = [f"use iam: {securityPillar()} to provide access", 'You can provide access to resources to both users and other AWS soervices', ]
    

def goals():
    ableTodescribe = ['key services on the AWS platform and their common use cases', 'Basic security and compliance aspects of the AWS platform and the shared security model', 'Basic/core characteristics of deploying and operating in the AWS Cloud']
    ableToIdentify = 'Sources of documentation or technical assistance'


def secondDomain():
    examGoal = ['Makes up 25% of the exam', 
                'Define the AWS shared responsibility model',
                'Define the AWS Cloud security and compliance concepts'
                'Identify AWS access management capabilities'
                'Identify resources for receiving security related support']
    
def infraestructurelooklike():
    nowAdays = ['Global network of data centers built with security in mind'
                'Safeguards to protect customer privacy'
                'Dozens of compliance programs to help meet industry compliance requirements for data security']
     
    awsAlowsyouTo = ['High-security standards without need for your own data centers', 'Scale your business quickly']


def securityResponsabilities():
    sharedResponsabilityModel = ['AWS = At the cloud', 'User = In the cloud']


def securityServices():
    
    def identityandAccessManagement():
        conceptIAM = ['Manage access to services and resources on the AWS Cloud', 'Manage users and groups', 'Can provide access to users or other AWS services', 'Permissions are global: any access setting will be true across all legions', 'Follow principle of least privilege']
        usingIAM = ['Manage Users', 'Manage IAM roles', 'Manage Federated Users']
        methodsIAM = [manageUsersIAM, manageIAMroles, manageFederatedUsers]
        manageUsersIAM = ['Create users in IAM and assign them security credentials', 'Users can have very precise permission sets', 'User can access AWS through AWS Management Console', 'You can provide programmatic access to data/resources', 'Programmatic access: applications directly accessing resources instead of humans doing the same activity']
        manageIAMroles = ['Create roles to manage permissions and what those roles can do', 'An entity assumes a role to obtain temporary security credentials to make API calls to your resources', 'Used to provide access to a user from another AWS account to your AWS account']
        manageFederatedUsers = ['Enable identity federation: allow existing identities in your enterprise to access AWS without having to create IAM user for each identityIdeal for lists', 'Can use any identity management solution using SAML 2.0 or one of AWSs federation samples', 'tip: using a gmail account to access other service in web is an example']
        benefitsIAM = ['Enhanced security', 'Granular control', 'Ability to provide temporary credentials', 'Flexible security credential management', 'Federated access', 'Seamless integration across various AWS services']

    def webApplicationFirewall():
        conceptWAF = ['Protects web apps running on the AWS Cloud from common web exploits', 'Firewall service for web applications', 'Protect web apps against exploits that could compromise security or availability', 'Protect apps from exploits that could force your app to consume excessive resources']
        usingWAF = ['Improves web traffic visibility', 'Provides cost-effective web app protection', 'Delivers increased security and protection against web attacks', 'Easy to deploy and maintain']

    def shield():
        DDoSattack = ['Distributed Denial of Service Attack', 'An attempt to make a machine or network resource unavailable' ,'Most often by making excessive repeated requests to the website using thousands of unique IP addresses']
        conceptShield = ['Provides detection and automatic mitigations', 'Minimizes effects of DDoS attacks to your apps', 'Helps minimize application downtime and latency when an attack happens']
        tiersShield = [standardShield,]
        standardShield = ['Automatically enabled', 'Free', 'Protects web applications against a majority of common DDoS attacks', 'Used with CloudFront and Rout 53, you can get comprehensive availability protection agains all known infrastructure attacks']
        advancedShield = ['Continuous 24/7 access to AWS DDoS response team', 'Near real-time visibility into events', 'Integrates with AWS WAF', 'Provides higher-level protections, network and transport layer protections, and automated application traffic monitoring', 'Provides financial protection against DDoS-related spikes in charges for EC2, elastic load balancers, CloudFront and Rout 53', 'Available globally on all CloudFront and Route 53 Edge locations', 'your web application can be hosted anywhere in the world and still be protected by AWS Shield']
        usingShield = ['Comprehensive protection against DDoS catered to your budget and needs']

    def amazonInspector():
        conceptInspector = ['Automated security assessment service for applications', 'Automatically assess for exposure, vulnerabilities, and derivations from best practices', 'Generates detailes reports to help check for vulnerabilities', 'Security teams can get reports validating thats testes were performed']
        usingInspector = ['Reduce risk of introducing security issues during deployment and development', 'You can define standards and best practices', 'OR use the AWS constantly updated standards', 'Amazon Inspector: Inspects your applications to find security issues']
    
    def trustedAdvisor():
        conceptTrustedAdvisor = ['Guides provisioning of resources to follow AWS best Practices', 'Scans your infrastructure and advises you on how it is or is not following AWS best practices', F"Based on five categories: {bestPracices}", 'Provides action recommendations to meet best practices']
        bestPracices = ['Cost optimization', 'performance', 'security', 'fault tolarance', 'service limits']
        sevenCoreTrustedAdvisorChecks = ['S3 Buckets permissions', 'Security groups - specific ports unrestricted', 'IAM use', 'MFA on root account', 'EBS public snapshots', 'RDS public snapshots', 'Service limits']
        FullTrustedAdvisorChecks = ['AWS enterprise or business plans', f"More types of checks on top of {sevenCoreTrustedAdvisorChecks}", 'Notifications through weekly updates', 'Hability to set up automated actions in response to alerts using CloudWatch', 'Programmatic access to scan results via AWS Support API']
        goal = 'Makes sure AWS Cloud resources are aligned with best practices and provide customizes recommendations'

    def guardDuty():
        conceptGuardDuty = ['24/7 threat detection service for the AWS Cloud', 'Monitors for malicious activity and unauthorized behavior', 'Analyzes events to send actionable alerts via CloudWatch', 'Uses machine learning, anomaly detection, and integrated threat intelligence to identify potencial threats', 'Easy to Deploy']
        goal = 'Amazon GuardDuty continuously monitors your AWS Cloud infraestructure, intelligently detects threats using machine learning, and helps you take action immediately if a threat is found'
        
    def review():
        awsIAM = ['Securely manage access to services and resources in AWS with extremely granular permissions sets', 'Set access permissions for users or other services to a resource', 'Create an manage IAM roles with specific permission sets', 'Dont have to manually set every entitys permission sets, wich could result in inconsistencies', 'Utilize identity deferation for already existing users in non-AWS services']
        awsWAF = ['Firewall for web applications running on the AWS Cloud','Protects web apps from common web exploits and potential compromises that can jack up your AWS usage bill', 'Improves traffic visibility','Can be deployed within minutes']
        awsSHIELD = ['Detection and automatic mitigations of distributed denial of service (DDoS) attacks to web applications','Standard tier: automatic, free, Protects agains majority of common DDos Attacks','Advanced tier: Continuous 24/07 access DDoS response team, Detects and mitigates sophisticated DDoS attacks, Provides financial protection against DDoS-related spikes in AWS resources usages']
        amazonINSPECTOR= ['Automated security assessment service to improve security and compliance', 'Automatically assesses applications for exposure, vulnerabilities, and derivations from best practices', 'Generated detailed reports', 'Define standards to check against and create reports to validate specific test were performed']
        awsTRUSTEDADVISOR = ['Guides resource provisioning to align with AWS best practices', 'Advises you on how your infrastructure is or is not following AWS best practices, based on five categories: Optimization, Performance, Security, Fault tolerance, Service limits', 'Seven core Trusted Advisor checks are free', 'Full Trusted Advisor checks are free with Business Support plans and above']
        amazonGUARDDUTY = ['Threat detection service that monitors for malicious activity and unauthorized behavior non-stop, 24/7', 'Identifies and prioritizes potential threats', 'Quick to deploy']



