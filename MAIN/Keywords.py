# Define general keywords that could be present across various document types
general_keywords = [
    "document",
    "file",
    "report",
    "letter",
    "email",
    "memo",
    "name",
    "address",
    "phone number",
    "email address",
    "date",
    "time",
    "subject",
    "attachment",
    "reference",
    "company",
    "organization",
    "department",
    "customer",
    "total",
    "amount",
    "payment",
    "invoice",
    "receipt",
    "description",
    "prescription",
    "notes",
    "terms and conditions",
    "signature",
    "approved",
    "rejected",
    "pending",
    "completed",
    "cancelled",
    "true",
    "false",
    "yes",
    "no",
    "on",
    "off",
    "high",
    "low",
    "important",
    "urgent",
    "confidential",
]

# Define specific keyword lists for invoice document types
invoice_keywords = [
    "invoice",
    "bill",
    "receipt",
    "statement",
    "number",
    "date",
    "company name",
    "customer name",
    "billing address",
    "shipping address",
    "item",
    "description",
    "product",
    "service",
    "quantity",
    "unit price",
    "total price",
    "amount",
    "cost",
    "line item",
    "payment terms",
    "payment method",
    "subtotal",
    "tax",
    "vat",
    "gst",
    "total due",
    "balance due",
    "paid",
    "purchase order",
    "order number",
    "sales order",
    "sku",
    "uom",  # Unit of Measure
    "discount",
    "shipping and handling",
    "terms and conditions",
    "notes",
    "authorized signature",
    "labor costs",
    "material costs",
    "change order",
    "retainer",
    "service fee",
    "court fees",
    "billable hours",
    "software license",
    "maintenance fee",
    "subscription fee",
    "finance charge",
    "late fee",
    "interest",
    "account number",
    "payment reference",
    "credit memo",
    "debit memo",
    "refund",
    "adjustment",
    "return",
    "sales tax",
    "shipping cost",
    "insurance cost",
    "warranty",
    "guarantee",
    "reference number",
    "tracking number",
    "net pay",
    "employee name",
    "department",
    "due upon receipt",
]

# Define specific keyword lists for prescription document types
prescription_keywords = [
    "Rx",
    "dispense",
    "patient name",
    "doctor name",
    "pharmacy",
    "medication",
    "drug name",
    "generic name",
    "dosage",
    "strength",
    "form",
    "quantity",
    "refills",
    "directions",
    "instructions",
    "diagnosis",
    "sig",
    "prn",  # As Needed
    "as needed",
    "take with food",
    "avoid alcohol",
    "discontinue if",
    "side effects",
    "allergies",
    "not for use with",
    "expiration date",
    "mg",  # Milligrams
    "ml",  # Milliliters
    "tab",  # Tablet
    "cap",  # Capsule
    "g",  # Grams
    "mcg",  # Micrograms
    "BID",  # Twice a Day
    "TID",  # Three Times a Day
    "QID",  # Four Times a Day
    "HS",  # Before Sleep
    "PO",  # By Mouth
    "IM",  # Intramuscular
    "SQ",  # Subcutaneous
    "PRN",  # As Needed (another way to write it)
    "ASA",  # Aspirin
    "OTC",  # Over-the-Counter
]

# Define specific keyword lists for labreports document types
lab_report_keywords = [
    "lab report",
    "laboratory report",
    "test results",
    "date",
    "patient name",
    "doctor name",
    "lab name",
    "accession number",
    "reference number",
    "specimen type",
    "test name",
    "test code",
    "panel",
    "profile",
    "analyte",
    "method",
    "reference range",
    "units",
    "result",
    "abnormal",
    "normal",
    "flag",
    "diagnosis",
    "impression",
    "interpretation",
    "recommendation",
    "comments",
    "performed by",
    "reviewed by",
    "released by",
    "CBC",  # (Complete Blood Count)
    "BMP",  # (Basic Metabolic Panel)
    "CMP",  # (Comprehensive Metabolic Panel)
    "HDL",  # (High-Density Lipoprotein)
    "LDL",  # (Low-Density Lipoprotein)
    "AST",  # (Aspartate Aminotransferase)
    "ALT",  # (Alanine Aminotransferase)
    "PSA",  # (Prostate-Specific Antigen)
    "WBC",  # (White Blood Cell Count)
    "RBC",  # (Red Blood Cell Count)
    "Hgb",  # (Hemoglobin)
    "Hct",  # (Hematocrit)
    "PLT",  # (Platelet Count)
    "MCHC",  # (Mean Corpuscular Hemoglobin Concentration)
    "MCH",  # (Mean Corpuscular Hemoglobin)
    "MCV",  # (Mean Corpuscular Volume)
    "RDW",  # (Red Cell Distribution Width)
    "Na",  # (Sodium)
    "K",  # (Potassium)
    "Cl",  # (Chloride)
    "CO2",  # (Carbon Dioxide)
    "BUN",  # (Blood Urea Nitrogen)
    "Cr",  # (Creatinine)
    "Gluc",  # (Glucose)
    "Ca",  # (Calcium),  # Common lab test abbreviations
]
