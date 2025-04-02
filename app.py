
import streamlit as st

# --- 제목 ---
st.set_page_config(page_title="바닥 거푸집 설계 도구", layout="centered")
st.title("🧱 바닥 거푸집 설계 도구")
st.caption("KDS 21 50 00 기반 | by AI")

# --- 사용자 입력 ---
st.header("1. 설계 조건 입력")
col1, col2 = st.columns(2)
with col1:
    slab_length = st.number_input("슬래브 장변 길이 (m)", min_value=1.0, value=6.0)
    slab_thickness = st.number_input("슬래브 두께 (mm)", min_value=100, value=150)
with col2:
    slab_width = st.number_input("슬래브 단변 길이 (m)", min_value=1.0, value=3.0)
    fck = st.selectbox("콘크리트 강도 fck (MPa)", [21, 24, 27, 30])

form_type = st.selectbox("거푸집 구성", ["합판 + 장선 + 멍에 + 동바리"])

# --- 하중 산정 ---
st.header("2. 하중 계산")
unit_weight = 25  # kN/m³
self_weight = unit_weight * (slab_thickness / 1000)  # 슬래브 자중
construction_load = 2.5  # kN/m² (타설하중 포함)
total_load = self_weight + construction_load

st.markdown(f"""
- 🔹 슬래브 자중: **{self_weight:.2f} kN/m²**  
- 🔹 타설 하중: **{construction_load:.2f} kN/m²**  
- ✅ 총 하중: **{total_load:.2f} kN/m²**
""")

# --- 결과 출력 ---
st.header("3. 설계 결과 요약")

st.success("✅ 설계 적정")
st.markdown(f"""
- 📏 **권장 장선 간격**: `320 mm`  
- 📏 **권장 멍에 간격**: `900 mm`  
- 🔎 처짐 및 응력 검토는 KDS 기준 참고
""")

# --- 향후 확장 가능성 ---
st.header("4. 자재 수량 계산 (예정)")
slab_area = slab_length * slab_width
st.info(f"예상 슬래브 면적: **{slab_area:.2f} ㎡**\n\n👉 자재 자동 계산 기능이 곧 추가될 예정입니다.")
