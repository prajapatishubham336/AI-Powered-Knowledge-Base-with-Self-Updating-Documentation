from pathlib import Path
from services.database import init_db, save_document
import hashlib
DB=Path("data/knowledge.db"); DB.parent.mkdir(exist_ok=True); init_db(DB)
docs={
"Payment API Guide.md":"Payment API authentication uses an API key in the Authorization header. Rotate keys every 90 days. Failed authentication returns HTTP 401.",
"Vendor Management Guidelines.md":"Vendors must pass security review before production access. Reviews are renewed annually and critical vendors require quarterly checks.",
"Onboarding Process Overview.md":"New employees complete identity verification, security training and product onboarding before receiving production access.",
"Industry Regulations.md":"Customer data must be handled according to applicable privacy and security regulations. Access should follow least privilege.",
"Pricing and Discounts Matrix.md":"Enterprise discounts require account approval. Billing changes should be documented and reflected in the customer contract."
}
for name,text in docs.items():
    save_document(DB,name,hashlib.sha256(text.encode()).hexdigest(),len(text),text)
print("Demo knowledge documents added.")
