"""
김도연 — Portfolio
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="김도연 | Portfolio",
    page_icon="○",
    layout="wide",
    initial_sidebar_state="expanded",
)

INK = "#0F172A"
SUB = "#475569"
MUTED = "#94A3B8"
LINE = "#E2E8F0"
ACCENT = "#1E3A8A"

st.markdown(f"""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');

html, body, [class*="css"] {{
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: {INK}; letter-spacing: -0.01em;
}}
.block-container {{padding-top: 3rem; padding-bottom: 3rem; max-width: 1160px;}}
h1, h2, h3, h4 {{font-weight: 600; letter-spacing: -0.025em; color: {INK};}}

.eyebrow {{
    font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: {MUTED}; font-weight: 500; margin-bottom: 0.5rem;
}}
.headline {{
    font-size: 2.3rem; font-weight: 700; color: {INK};
    line-height: 1.25; margin: 0 0 0.7rem 0; letter-spacing: -0.03em;
}}
.lead {{
    font-size: 1rem; color: {SUB}; line-height: 1.7; font-weight: 400;
    max-width: 720px;
}}

.kpi {{
    border: 1px solid {LINE}; border-radius: 4px;
    padding: 1.3rem 1.4rem; background: white;
}}
.kpi-value {{font-size: 1.6rem; font-weight: 700; color: {INK}; line-height: 1.15; letter-spacing: -0.02em;}}
.kpi-label {{font-size: 0.78rem; color: {MUTED}; margin-top: 0.45rem; letter-spacing: 0.02em;}}

.card {{
    border: 1px solid {LINE}; border-radius: 4px;
    padding: 1.6rem 1.6rem; background: white; height: 100%;
}}
.card h4 {{margin: 0 0 0.6rem 0; font-size: 0.95rem; color: {INK}; font-weight: 600;}}
.card p  {{margin: 0; font-size: 0.88rem; color: {SUB}; line-height: 1.7;}}

.project {{border-top: 1px solid {LINE}; padding: 2rem 0 0.5rem 0;}}
.project-num {{
    font-size: 0.72rem; letter-spacing: 0.14em;
    color: {MUTED}; font-weight: 500;
}}
.project-title {{
    font-size: 1.2rem; font-weight: 600; color: {INK};
    margin: 0.3rem 0 0.6rem 0; letter-spacing: -0.02em;
}}
.project-sub {{font-size: 0.9rem; color: {SUB}; margin-bottom: 1.4rem; line-height: 1.6;}}

.label {{
    font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: {MUTED}; font-weight: 500; margin-bottom: 0.6rem;
}}
.body {{font-size: 0.88rem; color: {INK}; line-height: 1.75;}}
.body.muted {{color: {SUB};}}

section[data-testid="stSidebar"] {{background: white; border-right: 1px solid {LINE};}}
section[data-testid="stSidebar"] .block-container {{padding-top: 2.5rem;}}
div[data-testid="stRadio"] label {{font-size: 0.9rem; color: {SUB}; padding: 0.35rem 0;}}
.small {{font-size: 0.8rem; color: {MUTED}; line-height: 1.6;}}
.stDataFrame {{border: 1px solid {LINE}; border-radius: 4px;}}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"<div class='eyebrow'>Portfolio</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:1.3rem; font-weight:700; color:{INK};'>김도연</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:0.82rem; color:{SUB}; margin-top:0.15rem;'>NAVER Cloud · Cloud Product Synergy</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    section = st.radio(
        " ",
        ["개요", "경력", "역량", "프로젝트", "자격 · 학력"],
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='eyebrow'>Contact</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small'>jjuncco@naver.com<br>010-2079-0828<br>성남 분당구 서현</div>", unsafe_allow_html=True)

career = pd.DataFrame([
    {"회사": "NAVER Cloud", "조직": "Cloud Product Synergy", "시작": "2025-07", "종료": "2026-04",
     "개월": 10, "분야": "IT / SaaS", "역할": "NAVER WORKS 사업 운영관리"},
    {"회사": "용인세브란스병원", "조직": "사회사업팀", "시작": "2024-06", "종료": "2025-06",
     "개월": 12, "분야": "Healthcare", "역할": "응급실 자살시도자 사후관리사업 총괄"},
    {"회사": "분당서울대학교병원", "조직": "의료사회복지팀", "시작": "2023-01", "종료": "2024-05",
     "개월": 17, "분야": "Healthcare", "역할": "취약계층 자동의뢰 프로세스 기획 · 구축"},
    {"회사": "신촌세브란스병원", "조직": "사회사업팀", "시작": "2022-10", "종료": "2022-12",
     "개월": 3, "분야": "Healthcare", "역할": "소원트리 사회공헌 프로그램 운영"},
    {"회사": "서울특별시보라매병원", "조직": "의료사회복지팀", "시작": "2020-09", "종료": "2021-09",
     "개월": 13, "분야": "Healthcare", "역할": "서울시 안전망병원 사업 총괄"},
    {"회사": "가천대길병원", "조직": "사회사업팀", "시작": "2019-03", "종료": "2020-03",
     "개월": 13, "분야": "Healthcare", "역할": "임상 수련 (전국 1위 수상)"},
])

projects = [
    {
        "num": "01",
        "title": "B2B SaaS 릴리즈 커뮤니케이션 · 정산 운영",
        "company": "NAVER Cloud · NAVER WORKS",
        "sub": "다직군 산출물을 고객 언어로 번역하고, 억 단위 정산의 데이터 무결성을 확보합니다.",
        "problem": "매월 반복되는 업데이트마다 기획·개발·디자인 산출물을 고객이 이해할 수 있는 언어로 번역해야 했습니다. 월평균 억 단위 파트너사·사내 정산 데이터는 단 한 건의 오차가 운영 신뢰도를 훼손할 수 있는 구조였습니다.",
        "method": "팀 간 인터페이스 역할로 릴리즈노트와 서비스 가이드를 작성하고, 대시보드와 운영 툴 데이터를 교차 검증하는 정산 프로세스를 운영했습니다. 앱마켓 제휴사·공공 담당자와의 커뮤니케이션을 주도했습니다.",
        "results": [
            "억 단위 월 정산 — 오차 0건 마감",
            "선제적 릴리즈 커뮤니케이션으로 VOC 최소화",
            "범정부 클라우드 전환 사업 현장(애플타워) 지원 경험 확보",
        ],
    },
    {
        "num": "02",
        "title": "IT 기반 프로세스 혁신",
        "company": "분당서울대학교병원",
        "sub": "취약계층 자동 의뢰 시스템을 기획하고, 부서 간 이해관계를 조율해 전산화를 주도했습니다.",
        "problem": "수기 의뢰 방식은 의료진 업무 부담을 가중시키고, 지원 심사 대기가 평균 7일 소요되어 지원이 시급한 환자의 누락이 발생하는 구조였습니다.",
        "method": "입원 오더 발생 즉시 의료사회복지팀으로 자동 의뢰되는 프로세스를 제안하고, 의료진·원무팀·의료정보팀 간 이해관계를 조율하며 전산화를 주도했습니다.",
        "results": [
            "심사 대기 기간 7일 → 3일 단축 (-57%)",
            "지원 대상자 발굴 증가 및 의료진 행정 부담 완화",
            "병원 표준 의뢰 프로세스로 현재까지 정착",
        ],
    },
    {
        "num": "03",
        "title": "정책 사각지대 발굴 및 제도 확장",
        "company": "서울특별시보라매병원",
        "sub": "현장 근거를 기반으로 Bottom-up 정책 개선을 이끌었습니다.",
        "problem": "서울시 안전망병원 지원사업은 응급·수술 등 중증질환 중심이었습니다. 중증 장애인·노인의 치주·치과 질환은 섭식 장애와 전신 건강 악화로 이어지는데도 지원 대상에서 제외되어 있었습니다.",
        "method": "임상 사례와 의료진 소견을 근거로 서울시청·보건복지부를 대상으로 지원 필요성을 설득했습니다. 신규 사업 도입 시 현장 적용 가능성을 검증하는 테스트베드 역할을 수행했습니다.",
        "results": [
            "치주 질환까지 지원 범위 확대",
            "현장 근거 기반 제도 개선 사례 확보",
        ],
    },
    {
        "num": "04",
        "title": "국가 사업 운영 · 표준화 체계 구축",
        "company": "용인세브란스병원",
        "sub": "자살시도자 사후관리 사업의 기획·예산·운영·결과보고 전반을 주도했습니다.",
        "problem": "응급실 내원 자살시도자는 재시도 위험이 높은 고위험군으로, 퇴원 후 지역사회 연결고리가 끊길 경우 재발이 반복되는 구조였습니다.",
        "method": "응급의학과·정신건강의학과와 협업해 초기 평가·사례관리를 총괄하고, 국가 시스템과 원내 데이터 기반 고위험군 선별·모니터링 체계를 제안했습니다. 2024 권역정신응급의료센터 심포지엄에 운영 결과를 발표하고 매뉴얼을 유관기관에 배포했습니다.",
        "results": [
            "사례관리 동의율 71.7% — 전국 평균(66.2%) 상회",
            "지역사회 연계를 통한 자살 예방 안전망 강화",
            "국고보조금 예산 편성 · 결산 · 결과보고 전반 리딩",
        ],
    },
]

def section_header(eyebrow, headline, lead=None):
    st.markdown(f"<div class='eyebrow'>{eyebrow}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='headline'>{headline}</div>", unsafe_allow_html=True)
    if lead:
        st.markdown(f"<div class='lead'>{lead}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

if section == "개요":
    section_header(
        "Profile",
        "임상 현장의 엄밀함과 SaaS의 속도를 함께 운영합니다.",
        "대학병원 임상 실무에서 NAVER Cloud B2B SaaS 운영까지 6년 이상의 교차 경력. "
        "사용자가 실제로 적응하고 성장하는 시스템을 설계합니다.",
    )

    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        ("6년+", "운영 실무 경력"),
        ("억 원 규모", "월 정산 · 오차 0건"),
        ("-57%", "의뢰 프로세스 단축"),
        ("전국 1위", "수련 평가 수상"),
    ]
    for col, (v, l) in zip([c1, c2, c3, c4], kpis):
        with col:
            st.markdown(f"<div class='kpi'><div class='kpi-value'>{v}</div><div class='kpi-label'>{l}</div></div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("<div class='label'>포지셔닝</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='body'>Medical → Tech. 임상 현장에서 길러진 문제 해결의 깊이와 IT 운영의 속도를 "
            "함께 구사합니다. 보수적 조직(병원)에 시스템을 안착시킨 변화 관리 경험과, "
            "NAVER WORKS 운영을 통해 확보한 B2B SaaS 릴리즈·파트너·정산 운영에 대한 실무 이해를 갖추고 있습니다.</div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown("<div class='label'>지원 방향</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='body muted'>"
            "사업운영관리 · 서비스 운영 · 플랫폼 운영기획<br>"
            "B2B SaaS · 클라우드 · 헬스케어 IT<br>"
            "분당 · 판교 · 성남 (정규직)"
            "</div>",
            unsafe_allow_html=True,
        )

elif section == "경력":
    section_header(
        "Experience",
        "헬스케어에서 테크까지, 6년의 경력 궤적.",
        "대학병원 의료사회복지 실무에서 클라우드 제품 운영까지 — 모든 역할이 시스템 사고, 이해관계자 정렬, 측정 가능한 성과를 기반으로 이어집니다.",
    )

    df = career.copy()
    df["시작_dt"] = pd.to_datetime(df["시작"])
    df["종료_dt"] = pd.to_datetime(df["종료"])

    fig = px.timeline(
        df, x_start="시작_dt", x_end="종료_dt", y="회사",
        color="분야", text="역할",
        color_discrete_map={"IT / SaaS": ACCENT, "Healthcare": "#64748B"},
        hover_data={"조직": True, "개월": True, "시작_dt": False, "종료_dt": False},
    )
    fig.update_yaxes(autorange="reversed", title=None, tickfont=dict(size=11, color=SUB))
    fig.update_xaxes(tickfont=dict(size=11, color=SUB))
    fig.update_traces(textfont=dict(size=10, color="white"))
    fig.update_layout(
        height=380, margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="h", yanchor="bottom", y=1.04, xanchor="right", x=1, title=None, font=dict(size=11)),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='label'>상세 이력</div>", unsafe_allow_html=True)
    st.dataframe(
        df[["회사", "조직", "시작", "종료", "역할"]],
        hide_index=True, use_container_width=True,
    )

elif section == "역량":
    section_header(
        "Strengths",
        "도메인을 관통하는 세 가지 역량.",
        "임상과 운영 경험이 수렴하는 세 가지 전이 가능한 강점 — 기술 이해도, 변화 관리, 다이해관계자 커뮤니케이션.",
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        ("01  SaaS Lifecycle 이해",
         "NAVER WORKS 운영을 통해 릴리즈 사이클 · 파트너 정산 · 제품 커뮤니케이션에 대한 실무 감각을 확보했습니다."),
        ("02  실전형 변화 관리",
         "보수적 조직에서 수기 관행을 데이터 기반 근거로 설득해 전산 시스템을 안착시킨 경험을 보유하고 있습니다."),
        ("03  공공 · 민간 하이브리드 소통",
         "범정부 클라우드 전환 사업 현장 지원을 통해 임상·개발·파트너·공공 사이의 번역 역할을 수행했습니다."),
    ]
    for col, (title, body) in zip([c1, c2, c3], cards):
        with col:
            st.markdown(f"<div class='card'><h4>{title}</h4><p>{body}</p></div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div class='label'>역량 프로파일</div>", unsafe_allow_html=True)

    skills = pd.DataFrame([
        {"역량": "B2B SaaS 운영", "수준": 9},
        {"역량": "데이터 정합성", "수준": 9},
        {"역량": "이해관계자 커뮤니케이션", "수준": 9},
        {"역량": "릴리즈 관리", "수준": 8},
        {"역량": "프로세스 설계", "수준": 9},
        {"역량": "예산 · 정산 운영", "수준": 9},
        {"역량": "헬스케어 도메인", "수준": 10},
        {"역량": "공공정책 이해", "수준": 8},
    ])
    fig = go.Figure(data=go.Scatterpolar(
        r=skills["수준"], theta=skills["역량"], fill='toself',
        line=dict(color=ACCENT, width=1.5),
        fillcolor="rgba(30, 58, 138, 0.12)",
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], showticklabels=False, gridcolor=LINE),
            angularaxis=dict(gridcolor=LINE, tickfont=dict(size=11, color=SUB)),
            bgcolor="white",
        ),
        showlegend=False, height=440,
        margin=dict(l=60, r=60, t=20, b=20),
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)

elif section == "프로젝트":
    section_header(
        "Projects",
        "문제와 시스템이 만나는 네 개의 지점.",
        "NAVER Cloud와 세 곳의 대학병원에서 수행한 주요 과제 — 현장 근거에 기반하고 다부서 협업을 통해 실행했습니다.",
    )

    for p in projects:
        st.markdown(f"<div class='project'>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-num'>PROJECT {p['num']}  ·  {p['company']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-title'>{p['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-sub'>{p['sub']}</div>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3, gap="medium")
        with c1:
            st.markdown("<div class='label'>배경</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='body muted'>{p['problem']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='label'>접근</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='body muted'>{p['method']}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='label'>성과</div>", unsafe_allow_html=True)
            bullets = "".join([f"<li style='margin-bottom:0.5rem;'>{r}</li>" for r in p["results"]])
            st.markdown(f"<ul class='body' style='margin:0; padding-left:1.1rem;'>{bullets}</ul>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

elif section == "자격 · 학력":
    section_header(
        "Credentials",
        "학력 · 자격 · 부가 이력.",
    )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("<div class='label'>학력</div>", unsafe_allow_html=True)
        st.markdown("<div class='body'><b>가천대학교</b><br><span class='small'>2015.03 – 2019.02 졸업</span></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='label'>해외 경험</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='body muted'>"
            "하와이대학교 단기해외수업 · 2017<br>"
            "Northwest University (Seattle) 단기해외수업 · 2016<br>"
            "인터내셔널 프론티어 최우수상 (교내 1위) · 2017"
            "</div>", unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='label'>봉사</div>", unsafe_allow_html=True)
        st.markdown("<div class='body muted'>자원봉사 총 352시간 (2013 – 2024)</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='label'>자격증</div>", unsafe_allow_html=True)
        certs = pd.DataFrame([
            {"자격증": "사회복지사 1급", "영역": "Healthcare"},
            {"자격증": "의료사회복지사", "영역": "Healthcare"},
            {"자격증": "컴퓨터활용능력 2급", "영역": "IT"},
            {"자격증": "Essentials of Global Health", "영역": "Healthcare"},
            {"자격증": "TOEIC 890", "영역": "Language"},
            {"자격증": "TEPS 466", "영역": "Language"},
        ])
        st.dataframe(certs, hide_index=True, use_container_width=True)
