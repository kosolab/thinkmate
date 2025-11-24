import streamlit as st
from datetime import datetime
import time

# 페이지 설정
st.set_page_config(
    page_title="Think Mate (씽크메이트)",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 프리미엄 CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap');

    * {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #f8f9fe 0%, #e8eaf6 100%);
    }

    .main .block-container {
        max-width: 420px;
        padding: 1.5rem;
    }

    /* 카드 스타일 */
    div[data-testid="stMarkdownContainer"] > div {
        animation: fadeIn 0.3s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 버튼 스타일 */
    .stButton > button {
        width: 100%;
        border-radius: 16px;
        padding: 18px;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }

    /* 헤더 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 네비게이션 스타일 */
    .nav-container {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 420px;
        background: white;
        padding: 12px;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.1);
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'current_place' not in st.session_state:
    st.session_state.current_place = '푸른솔 놀이터'
if 'chat_step' not in st.session_state:
    st.session_state.chat_step = 0
if 'visit_data' not in st.session_state:
    st.session_state.visit_data = {}
if 'history' not in st.session_state:
    st.session_state.history = [
        {'place': '꿈나무 유치원 앞', 'date': '어제', 'lead': '1~2명', 'contract': '계약 1건'}
    ]

# 페이지 전환
def change_page(page_name):
    st.session_state.page = page_name
    if page_name == 'chat':
        st.session_state.chat_step = 0

# 홈 페이지
def render_home():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("##### 반갑습니다,")
        st.markdown("## 🔵 **김씽크** 님")
        st.caption("오늘도 힘내세요! 💪")

    with col2:
        st.markdown("""
        <div style="background: white; padding: 16px; border-radius: 16px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div style="font-size: 12px; color: #888; font-weight: bold;">7월 달성 현황</div>
            <div style="font-size: 20px; font-weight: 800; margin-top: 4px;">
                13 <span style="font-size:14px; color:#999;">/ 30개</span>
            </div>
            <div style="font-size: 13px; color: #00C853; font-weight: bold; margin-top: 2px;">
                43% 달성 📈
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 대시보드 카드
    st.markdown("""
    <div style="background: white; padding: 28px; border-radius: 20px;
                margin-bottom: 20px; box-shadow: 0 8px 24px rgba(0,70,255,0.08);">
        <div style="display:flex; justify-content:space-between; margin-bottom: 24px;">
            <div>
                <div style="font-size: 15px; color: #6b7280; font-weight: 600;">오늘 신규 목표</div>
                <div style="font-size: 36px; font-weight: 900; color: #0046FF; margin-top: 8px;">
                    5 <span style="font-size:20px; color:#9ca3af;">건</span>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 15px; color: #6b7280; font-weight: 600;">진단 목표</div>
                <div style="font-size: 36px; font-weight: 900; color: #0046FF; margin-top: 8px;">
                    2 <span style="font-size:20px; color:#9ca3af;">건</span>
                </div>
            </div>
        </div>
        <hr style="border:0; border-top:2px solid #f3f4f6; margin: 20px 0;">
        <div style="display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:17px; font-weight:700;">📅 오늘 예정 일정</span>
            <span style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
                         color:white; padding:6px 14px; border-radius:24px;
                         font-weight:800; font-size:15px;">3</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 메인 액션 버튼
    col1, col2 = st.columns([1, 2])

    with col1:
        if st.button("📅\n\n일정 등록", key="schedule_btn"):
            st.toast("일정 등록 화면")

    with col2:
        if st.button("🚀\n\nAI 장소 추천", key="ai_btn", type="primary"):
            change_page('recommend')
            st.rerun()

    if st.button("🛍️ 클로징 / 입회 확정", key="closing_btn"):
        st.toast("클로징/입회 확정 화면")

# AI 추천 페이지
def render_recommend():
    st.markdown("## 📍 AI 추천 핫스팟")

    # 지도
    st.markdown("""
    <div style="width: 100%; height: 220px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 20px; margin: 20px 0;
                display: flex; align-items: center; justify-content: center;
                box-shadow: 0 8px 24px rgba(102,126,234,0.3);">
        <div style="font-size: 60px;">📍</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🤖 지금 가면 딱 좋은 곳")

    if st.button("🔥 **푸른솔 놀이터**\n\n🕒 14:00~16:00 유동인구 급증", key="place1"):
        st.session_state.current_place = '푸른솔 놀이터'
        st.success("✅ 푸른솔 놀이터가 선택되었습니다!")

    if st.button("🚌 **꿈나무 유치원 앞**\n\n🕒 하원 버스 도착 시간", key="place2"):
        st.session_state.current_place = '꿈나무 유치원 앞'
        st.success("✅ 꿈나무 유치원 앞이 선택되었습니다!")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚘 카카오내비로 출발", key="navi_btn", type="primary"):
        st.balloons()
        st.success(f"📍 {st.session_state.current_place}로 출발합니다!")
        time.sleep(1)

# 챗봇 페이지
def render_chat():
    st.markdown("## 💬 AI 페이스메이트")
    st.caption("활동 결과를 간단히 기록해보세요")

    if st.session_state.chat_step == 0:
        st.info(f"**{st.session_state.current_place}**에는 잘 도착하셨나요?")
        st.write("오늘 활동 결과를 간단히 기록해볼까요? **리드(가망고객)**는 몇 분 만나셨나요?")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("0명", key="lead_0"):
                st.session_state.visit_data = {'lead': '0명'}
                st.session_state.chat_step = 1
                st.rerun()
        with col2:
            if st.button("1~2명", key="lead_1"):
                st.session_state.visit_data = {'lead': '1~2명'}
                st.session_state.chat_step = 1
                st.rerun()
        with col3:
            if st.button("3~5명", key="lead_3"):
                st.session_state.visit_data = {'lead': '3~5명'}
                st.session_state.chat_step = 1
                st.rerun()
        with col4:
            if st.button("5명+", key="lead_5"):
                st.session_state.visit_data = {'lead': '대박 (5명+)'}
                st.session_state.chat_step = 1
                st.rerun()

    elif st.session_state.chat_step == 1:
        st.success(f"리드: {st.session_state.visit_data['lead']}")
        st.write("고생 많으셨습니다! 👏 혹시 **진단이나 계약** 성과도 있었나요?")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("아직 없음", key="contract_0"):
                st.session_state.visit_data['contract'] = '아직 없음'
                st.session_state.chat_step = 2
                st.rerun()
        with col2:
            if st.button("진단 성공", key="contract_1"):
                st.session_state.visit_data['contract'] = '진단 성공'
                st.session_state.chat_step = 2
                st.rerun()
        with col3:
            if st.button("계약 성공!", key="contract_2"):
                st.session_state.visit_data['contract'] = '계약 성공!'
                st.session_state.chat_step = 2
                st.rerun()

    elif st.session_state.chat_step == 2:
        st.success(f"리드: {st.session_state.visit_data['lead']}")
        st.success(f"성과: {st.session_state.visit_data['contract']}")

        if st.session_state.visit_data['contract'] == '아직 없음':
            st.info("괜찮습니다! 씨앗을 뿌린 거니까요 🌱")
        else:
            st.balloons()
            st.success("와우! 축하드립니다! 🎉")

        if st.button("✅ 마이페이지로 이동", key="goto_mypage", type="primary"):
            new_record = {
                'place': st.session_state.current_place,
                'date': '방금 전 (NEW)',
                'lead': st.session_state.visit_data['lead'],
                'contract': st.session_state.visit_data['contract']
            }
            st.session_state.history.insert(0, new_record)
            change_page('mypage')
            st.rerun()

# 마이페이지
def render_mypage():
    st.markdown("## 📂 나의 활동 기록")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 리스트 보기", key="list_view"):
            st.toast("📋 리스트 보기")
    with col2:
        if st.button("🗺️ 지도로 보기", key="map_view"):
            st.toast("🗺️ 지도 보기")

    st.markdown("<br>", unsafe_allow_html=True)

    for record in st.session_state.history:
        is_new = record['date'].startswith('방금')
        contract_tag = "" if record['contract'] == '아직 없음' else f"<span style='background: #FFF3E0; color: #E65100; padding: 8px 14px; border-radius: 12px; font-weight: 700; font-size: 13px; margin-left: 8px;'>{record['contract']}</span>"

        st.markdown(f"""
        <div style="background: white; padding: 24px; border-radius: 20px;
                    margin-bottom: 14px; box-shadow: 0 6px 20px rgba(0,70,255,0.08);">
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <strong style="font-size:18px;">{record['place']}</strong>
                <span style="color:{'#0046FF' if is_new else '#999'};
                             font-size:14px; font-weight:{'bold' if is_new else 'normal'};">
                    {record['date']}
                </span>
            </div>
            <div>
                <span style="background: #f3f4f6; color: #4b5563; padding: 8px 14px;
                             border-radius: 12px; font-weight: 600; font-size: 13px;">
                    리드 {record['lead']}
                </span>
                {contract_tag}
            </div>
        </div>
        """, unsafe_allow_html=True)

# 하단 네비게이션
def render_bottom_nav():
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🏠\n홈", key="nav_home", use_container_width=True):
            change_page('home')
            st.rerun()

    with col2:
        if st.button("💬\n결과입력", key="nav_chat", use_container_width=True):
            change_page('chat')
            st.rerun()

    with col3:
        if st.button("👤\n마이", key="nav_mypage", use_container_width=True):
            change_page('mypage')
            st.rerun()

# 메인
def main():
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'recommend':
        render_recommend()
    elif st.session_state.page == 'chat':
        render_chat()
    elif st.session_state.page == 'mypage':
        render_mypage()

    render_bottom_nav()

if __name__ == "__main__":
    main()
