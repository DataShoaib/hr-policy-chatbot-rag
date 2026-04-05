# this file holds your ground-truth question-answer pairs for RAGAS evaluation
# add as many pairs as you want, just keep the two lists the same length
# these should be real questions your HR policy documents can actually answer

dataset = {
    "question": [
        "What is the annual paid leave entitlement for employees?",
        "How many days notice is required before taking planned leave?",
        "What is the policy on sick leave?",
        "Can unused leave be carried forward to the next year?",
        "What is the maternity leave policy?",
        "What is the paternity leave policy?",
        "How does the company handle leave during probation period?",
        "What is the process for applying for emergency leave?",
        "Are employees entitled to leave encashment?",
        "What are the working hours as per company policy?",
    ],
    "answer": [
        "Employees are entitled to 18 days of paid annual leave per year.",
        "Employees must provide at least 3 days notice for planned leave requests.",
        "Employees are entitled to 12 days of sick leave per year with a medical certificate required after 3 consecutive days.",
        "Up to 10 unused leave days can be carried forward to the next calendar year.",
        "Female employees are entitled to 26 weeks of paid maternity leave as per the Maternity Benefit Act.",
        "Male employees are entitled to 15 days of paid paternity leave within 6 months of the child's birth.",
        "Leave entitlement is pro-rated during the probation period based on months completed.",
        "Emergency leave requests should be submitted to the HR portal and notified to the immediate manager within 24 hours.",
        "Employees can encash up to 30 days of accumulated leave at the time of resignation or retirement.",
        "Standard working hours are 9 AM to 6 PM Monday to Friday with a one hour lunch break.",
    ],
}
