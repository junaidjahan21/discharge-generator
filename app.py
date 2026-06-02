import streamlit as st
from docxtpl import DocxTemplate
from datetime import datetime

st.set_page_config(page_title="Discharge Summary Generator", layout="wide")

st.title("NEIGRIHMS Discharge Summary Generator")

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:
    admission_date = st.text_input("Admission Date")
    discharge_date = st.text_input("Discharge Date")
    ip_no = st.text_input("IP Number")
    cr_no = st.text_input("CR Number")
    ward = st.text_input("Ward")

with col2:
    bed_no = st.text_input("Bed Number")
    patient_name = st.text_input("Patient Name")
    age = st.text_input("Age")
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    address = st.text_area("Address")

st.header("Diagnosis")
diagnosis_text = st.text_area(
    "Diagnosis",
    help="Enter one diagnosis per line",
    height=150
)
st.header("Clinical History")

presenting_complaints = st.text_area(
    "Presenting Complaints",
    height=120
)

history_present_illness = st.text_area(
    "History of Present Illness",
    height=180
)

condition_discharge = st.text_area(
    "Condition During Discharge",
    height=100
)

st.header("Examination")

col1, col2 = st.columns(2)

with col1:
    bp = st.text_input("Blood Pressure")
    pulse = st.text_input("Pulse")
    spo2 = st.text_input("SpO2")
    temperature = st.text_input("Temperature")

with col2:
    pallor = st.text_input("Pallor")
    icterus = st.text_input("Icterus")
    clubbing = st.text_input("Clubbing")
    edema = st.text_input("Edema")

jvp = st.text_input("JVP")
lymph_nodes = st.text_input("Lymph Nodes")

rs_findings = st.text_area("Respiratory System Findings")
cvs_findings = st.text_area("Cardiovascular System Findings")
pa_findings = st.text_area("Per Abdomen Findings")
cns_findings = st.text_area("CNS Findings")
# =========================
# INVESTIGATIONS
# =========================

st.header("Investigations")

st.subheader("Hemogram")

col1, col2 = st.columns(2)

with col1:
    hb_adm = st.text_input("Hb (Admission)")
    pcv_adm = st.text_input("PCV (Admission)")
    tlc_adm = st.text_input("TLC (Admission)")
    platelet_adm = st.text_input("Platelets (Admission)")

with col2:
    hb_dis = st.text_input("Hb (Discharge)")
    pcv_dis = st.text_input("PCV (Discharge)")
    tlc_dis = st.text_input("TLC (Discharge)")
    platelet_dis = st.text_input("Platelets (Discharge)")

st.subheader("Renal Function")

col1, col2 = st.columns(2)

with col1:
    urea_adm = st.text_input("Urea (Admission)")
    creat_adm = st.text_input("Creatinine (Admission)")

with col2:
    urea_dis = st.text_input("Urea (Discharge)")
    creat_dis = st.text_input("Creatinine (Discharge)")

st.subheader("Electrolytes")

col1, col2 = st.columns(2)

with col1:
    na_adm = st.text_input("Na (Admission)")
    k_adm = st.text_input("K (Admission)")
    cl_adm = st.text_input("Cl (Admission)")

with col2:
    na_dis = st.text_input("Na (Discharge)")
    k_dis = st.text_input("K (Discharge)")
    cl_dis = st.text_input("Cl (Discharge)")
    
st.subheader("Liver Function Tests")

col1, col2 = st.columns(2)

with col1:
    tbil_adm = st.text_input("TBIL (Admission)")
    dbil_adm = st.text_input("DBIL (Admission)")
    ast_adm = st.text_input("AST (Admission)")
    alt_adm = st.text_input("ALT (Admission)")
    alp_adm = st.text_input("ALP (Admission)")
    tp_adm = st.text_input("Total Protein (Admission)")
    alb_adm = st.text_input("Albumin (Admission)")
    glob_adm = st.text_input("Globulin (Admission)")

with col2:
    tbil_dis = st.text_input("TBIL (Discharge)")
    dbil_dis = st.text_input("DBIL (Discharge)")
    ast_dis = st.text_input("AST (Discharge)")
    alt_dis = st.text_input("ALT (Discharge)")
    alp_dis = st.text_input("ALP (Discharge)")
    tp_dis = st.text_input("Total Protein (Discharge)")
    alb_dis = st.text_input("Albumin (Discharge)")
    glob_dis = st.text_input("Globulin (Discharge)")

st.subheader("Calcium / Magnesium / Phosphate")

col1, col2 = st.columns(2)

with col1:
    ca_adm = st.text_input("Calcium (Admission)")
    mg_adm = st.text_input("Magnesium (Admission)")
    phos_adm = st.text_input("Phosphate (Admission)")

with col2:
    ca_dis = st.text_input("Calcium (Discharge)")
    mg_dis = st.text_input("Magnesium (Discharge)")
    phos_dis = st.text_input("Phosphate (Discharge)")

st.subheader("Other Investigations")

crp = st.text_input("CRP")
procalcitonin = st.text_input("Procalcitonin")

ferritin = st.text_input("Ferritin")
vit_b12 = st.text_input("Vitamin B12")
folate = st.text_input("Folate")

vit_d = st.text_input("Vitamin D")
pth = st.text_input("PTH")

tsh = st.text_input("TSH")
ft4 = st.text_input("FT4")
ft3 = st.text_input("FT3")
st.subheader("Viral Markers")

hbsag = st.text_input("HBsAg")
anti_hcv = st.text_input("Anti HCV")
ictc = st.text_input("ICTC")

st.subheader("Urine / ECG / Imaging")

urine_re = st.text_area("Urine RE", height=80)

ecg = st.text_area("ECG", height=80)

cxr = st.text_area("Chest X-Ray", height=80)

usg = st.text_area("USG", height=80)
ct = st.text_area("CT Scan", height=80)
mri = st.text_area("MRI", height=80)
xray = st.text_area("Other X-Ray", height=80)

# =========================
# HOSPITAL COURSE
# =========================

st.header("Course in Hospital")

course_in_hospital = st.text_area(
    "Hospital Course",
    height=250
)

# =========================
# TREATMENT
# =========================

st.header("Treatment Advised")

medications_text = st.text_area(
    "Enter one medication per line",
    height=200,
    placeholder="""Tab Metformin 500 mg BD
Tab Telmisartan 40 mg OD
Tab Pantoprazole 40 mg OD"""
)

# =========================
# FOLLOW UP
# =========================

st.header("Follow Up")

followup_plan = st.text_area(
    "Follow Up Plan",
    height=150
)# =========================
# GENERATE DOCUMENT
# =========================

st.header("Generate Discharge Summary")

if st.button("Generate DOCX"):

    meds = [m.strip() for m in medications_text.split("\n") if m.strip()]

    
    doc = DocxTemplate("template.docx")
    diagnoses = [
    d.strip()
    for d in diagnosis_text.split("\n")
    if d.strip()
]

    context = {
        "ADMISSION_DATE": admission_date,
        "DISCHARGE_DATE": discharge_date,
        "IP_NO": ip_no,
        "WARD": ward,
        "BED_NO": bed_no,
        "CR_NO": cr_no,
        "NAME": patient_name,
        "AGE": age,
        "SEX": sex,
        "ADDRESS": address,

        "DIAGNOSES": diagnoses,
        "DISCHARGE_CONDITION": condition_discharge,
        "PRESENTING_COMPLAINTS": presenting_complaints,
        "HISTORY": history_present_illness,

        "BP": bp,
        "PULSE": pulse,
        "PULSE_CHARACTER": "",
        "SPO2": spo2,
        "TEMP": temperature,

        "PALLOR": pallor,
        "ICTERUS": icterus,
        "CLUBBING": clubbing,
        "EDEMA": edema,
        "LYMPH_NODES": lymph_nodes,
        "JVP": jvp,

        "RS_FINDINGS": rs_findings,
        "CVS_FINDINGS": cvs_findings,
        "PA_FINDINGS": pa_findings,
        "CNS_FINDINGS": cns_findings,

        "HB_ADM": hb_adm,
        "HB_DIS": hb_dis,
        "PCV_ADM": pcv_adm,
        "PCV_DIS": pcv_dis,

        "TLC_ADM": tlc_adm,
        "TLC_DIS": tlc_dis,
        "PLATELET_ADM": platelet_adm,
        "PLATELET_DIS": platelet_dis,

        "UREA_ADM": urea_adm,
        "UREA_DIS": urea_dis,
        "CREAT_ADM": creat_adm,
        "CREAT_DIS": creat_dis,

        "NA_ADM": na_adm,
        "NA_DIS": na_dis,
        "K_ADM": k_adm,
        "K_DIS": k_dis,
        "CL_ADM": cl_adm,
        "CL_DIS": cl_dis,

        "TBIL_ADM": tbil_adm,
        "TBIL_DIS": tbil_dis,
        "DBIL_ADM": dbil_adm,
        "DBIL_DIS": dbil_dis,

        "AST_ADM": ast_adm,
        "AST_DIS": ast_dis,
        "ALT_ADM": alt_adm,
        "ALT_DIS": alt_dis,
        "ALP_ADM": alp_adm,
        "ALP_DIS": alp_dis,

        "TP_ADM": tp_adm,
        "TP_DIS": tp_dis,
        "ALB_ADM": alb_adm,
        "ALB_DIS": alb_dis,
        "GLOB_ADM": glob_adm,
        "GLOB_DIS": glob_dis,

        "CA_ADM": ca_adm,
        "CA_DIS": ca_dis,
        "MG_ADM": mg_adm,
        "MG_DIS": mg_dis,
        "PHOS_ADM": phos_adm,
        "PHOS_DIS": phos_dis,

        "CRP": crp,
        "PROCALCITONIN": procalcitonin,

        "FERRITIN": ferritin,
        "VIT_B12": vit_b12,
        "FOLATE": folate,

        "VIT_D": vit_d,
        "PTH": pth,

        "TSH": tsh,
        "FT4": ft4,
        "FT3": ft3,

        "HBSAG": hbsag,
        "ANTI_HCV": anti_hcv,
        "ICTC": ictc,

        "URINE_RE": urine_re,
        "ECG": ecg,
        "CXR": cxr,

        "USG": usg,
        "CT": ct,
        "MRI": mri,
        "XRAY": xray,

        "COURSE_IN_HOSPITAL_AI": course_in_hospital,
        "FOLLOWUP_PLAN": followup_plan,

        "MEDICATIONS": meds,
    }
  
    doc.render(context)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    safe_name = patient_name.replace(" ", "_")

    output_file = f"generated/{safe_name}_{timestamp}.docx"

    doc.save(output_file)
    st.success("Discharge Summary Generated Successfully!")

    with open(output_file, "rb") as file:
            st.download_button(
            label="Download Discharge Summary",
            data=file,
            file_name=output_file.split("/")[-1],
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )   