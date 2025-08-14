""" Dictionary to generate data. """
field_list = {
    # Customer
    "customer_id": {
        "type": "int",
        "examples": [1, 2, 3],
        "description": "Unique identifier for each customer",
    },
    "customer_dob": {
        "type": "datetime",
        "format": "%Y-%m-%d %H:%M:%S",
        "examples": ["1990-01-01 00:00:00", "1995-06-15 12:00:00"],
        "description": "Date of birth for each customer",
    },
    "customer_country": {
        "type": "str",
        "examples": ["USA", "India", "Canada", "UK"],
        "description": "Country of residence for each customer",
    },
    "customer_state": {
        "type": "str",
        "examples": ["Texas", "Haryana", "New York", "California"],
        "description": "State of residence for each customer",
    },
    "customer_zip": {
        "type": "str",
        "examples": ["12345", "67890", "90210", "110001"],
        "description": "Zip code for each customer",
    },
    # Complaint
    "complaint_id": {
        "type": "int",
        "examples": [1, 2, 3],
        "description": "Unique identifier for each complaint",
    },
    "complaint_id_seq": {
        "type": "int",
        "examples": [1, 2, 3],
        "description": "Sequence number for each interaction within a complaint",
    },
    "complaint_interaction_date": {
        "type": "datetime",
        "format": "%Y-%m-%d %H:%M:%S",
        "examples": ["2025-01-01 20:10:06", "2025-01-02 21:11:07"],
        "description": "Date and time of each interaction",
    },
    "complaint_mode": {
        "type": "str",
        "examples": ["Fax", "Phone", "Email", "Web", "Post"],
        "description": "Mode of communication for each complaint",
    },
    "complaint_desc_short": {
        "type": "str",
        "examples": ["Side effect", "How to open medicine bottle", "Dosage issue"],
        "description": "Short description for the customer complaint",
    },
    "complaint_desc": {
        "type": "str",
        "examples": [
            "I was walking to the bathroom and opened the wig to see hair loss.",
            "The medicine bottle comes with a lock I am not sure can be opened without breaking the glass.",
            "I took the wrong dosage and now I'm feeling unwell.",
        ],
        "description": "Longer description for the complaint",
    },
    "complaint_desc_narrative": {
        "type": "str",
        "examples": [
            "It was few weeks ago I went to the doctor. The pain was in the knee. Late last week when I was walking to the bathroom and opened the wig to see hair loss.",
            "I purchased this 6 months ago. Had been busy so some time. The medicine bottle comes with a lock I am not sure can be opened without breaking the glass.",
            "I've been taking this medication for months, but recently I've been experiencing some side effects.",
        ],
        "description": "Multiline story about the issues customer faced",
    },
    "complaint_narrative_chain": {
        "type": "str",
        "examples": [
            "2025-05-08 20:04:06: [Agent 1] Received call from patient. \n\n 2025-05-08 20:08:06: It was few weeks ago I went to the doctor.",
            "2025-08-08 20:04:06: [Agent 121] Called patient. \n\n 2025-05-08 20:09:07: I purchased this 6 months ago.",
            "2025-02-02 10:00:00: [Agent 50] Email received from customer.",
        ],
        "description": "Multiline story by timestamp of all prior conversations related to the complaint",
    },
    "complaint_status": {
        "type": "str",
        "examples": ["Hold", "Ongoing", "Resolved", "Escalated"],
        "description": "Status of the complaint",
    },
    "complaint_code": {
        "type": "str",
        "examples": ["Self", "Endocrine", "Cardiovascular"],
        "description": "Medical code classifying the nature of the complaint",
    },
    "complaint_related_delivery": {
        "type": "int",
        "examples": [0, 1, 2, 5],
        "description": "Number of samples delivered that have the issue",
    },
    # Drug
    "drug_class": {
        "type": "str",
        "examples": ["Class 1", "Class 2", "Class 3"],
        "description": "Name of the drug class",
    },
    "drug_sub_class": {
        "type": "str",
        "examples": ["Sub Class 1", "Sub Class 2", "Sub Class 3"],
        "description": "Subclass within a unique drug class",
    },
    "drug_brand_name": {
        "type": "str",
        "examples": ["Brand 1", "Brand 2", "Brand 3"],
        "description": "Brand name of the drug",
    },
    "manufacturer": {
        "type": "str",
        "examples": ["Company 1", "Company 2", "Company 3"],
        "description": "Manufacturer of the drug",
    },
    "drug_batch_code": {
        "type": "int",
        "examples": [544, 6511, 1234],
        "description": "Batch number of the drug",
    },
    "drug_administration": {
        "type": "str",
        "examples": ["Oral", "Tablet", "Injection"],
        "description": "Mode of administration for the drug",
    },
    # Agent Response
    "agent_l1": {
        "type": "str",
        "examples": [
            "Issue acknowledged and escalated to medical watchlist.",
            "Issue transferred to product specification department.",
            "Customer has been informed about the possible side effects.",
        ],
        "description": "Short description of the agent's response",
    },
    # Company Response
    "company_response": {
        "type": "str",
        "examples": [
            "Company believes the complaint is the result of a misunderstanding.",
            "Company has responded to the consumer and the CFPB and chooses not to provide a public response.",
            "We apologize for the inconvenience and are working on a solution.",
        ],
        "description": "Formal note from the company related to the complaint",
    },
    # Dispute
    "customer_dispute": {
        "type": "str",
        "examples": ["Yes", "No"],
        "description": "Whether the customer disputes the company's response",
    },
    # Data Privacy
    "consent": {
        "type": "str",
        "examples": ["Yes", "No"],
        "description": "Whether the customer has given consent to share data for research",
    },
}







