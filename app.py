import streamlit as st
import pandas as pd
import plotly.express as px

# import model
from models.inventory import Inventory
from models.analytics import Analytics
from models.clustering import ProductClustering

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Helptory",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* ── Sembunyikan navigasi multipage otomatis Streamlit ── */
[data-testid="stSidebarNavItems"],
[data-testid="stSidebarNavSeparator"],
section[data-testid="stSidebarNav"],
div[data-testid="stSidebarNavItems"],
ul[data-testid="stSidebarNavItems"],
[data-testid="collapsedControl"] + div [data-testid="stSidebarNavItems"] {
    display: none !important;
}

/* Hilangkan label "Navigation" bawaan radio */
[data-testid="stSidebar"] label[data-baseweb="radio"] ~ div > div:first-child {
    display: none;
}
        
/* ── Sidebar background ── */
[data-testid="stSidebar"] {
    background-color: #14532d !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked) {
    background: rgba(255,255,255,0.15) !important;
    border-left: 4px solid #facc15 !important;
    color: white !important;
}

/* Sembunyikan label teks "Navigation" di atas radio */
[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

/* ── Tampilan radio button jadi menu kustom ── */
[data-testid="stSidebar"] .stRadio > div {
    gap: 0px !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    padding: 12px 20px !important;
    border-radius: 0px !important;
    border-left: 3px solid transparent !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    color: white !important;
    margin: 0 !important;
    background: transparent !important;
}

[data-testid="stSidebar"] .stRadio label p {
    color: white !important;
}

/* AKTIF — highlight kuning saja, tidak diperbesar */
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: rgba(250, 204, 21, 0.15) !important;
    border-left: 4px solid #86efac !important;
    color: #facc15 !important;
    font-weight: 700 !important;
}

/* Sembunyikan lingkaran radio asli */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label > div:first-child {
    display: none !important;
}

/* ── App background ── */
.stApp {
    background-color: #d1e0d1;
}

/* ── Heading color ── */
h1, h2, h3 {
    color: #000000;
}

/* ── Metric card ── */
[data-testid="metric-container"] {
    background-color: #dcfce7;
    border: 1px solid #bbf7d0;
    padding: 15px;
    border-radius: 15px;
}

/* ── Sidebar header area ── */
.sidebar-header {
    padding: 20px 16px 10px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 8px;
}

.sidebar-app-name {
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    margin: 0;
    padding: 0;
    letter-spacing: 0.3px;
}

.sidebar-app-sub {
    color: #86efac;
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.sidebar-section-label {
    color: #4ade80;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 14px 20px 6px 20px;
}

</style>
""", unsafe_allow_html=True)


# LOAD DATASET


df = pd.read_csv("data/sales_transactions.csv")
inventory_df = pd.read_csv("data/inventory_stock.csv")

# CREATE OBJECTS 


inventory = Inventory(inventory_df)
analytics = Analytics(df)
clustering = ProductClustering(df)

# SIDEBAR


with st.sidebar:

    #  Logo + Nama App 
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/logo_white.png", width=80)
    with col2:
        st.markdown(
            """
            <div style="
                display:flex;
                flex-direction:column;
                justify-content:center;
                height:90px;
            ">
                <p class='sidebar-app-name'>Helptory</p>
                <p class='sidebar-app-sub'>Retail Analytics</p>
            </div> 
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "<hr style='border:none;border-top:1px solid rgba(255,255,255,0.15);margin:10px 0 0 0;'>",
        unsafe_allow_html=True
    )

    # ── Label seksi ──
    st.markdown(
        "<div class='sidebar-section-label'>MENU UTAMA</div>",
        unsafe_allow_html=True
    )

    # ── Menu
    menu = st.radio(
        "Navigation",
        [
            "🏡 Dashboard",
            "📈 Analytics"
        ],
        label_visibility="collapsed"
    )


# HALAMAN DASHBOARD


if menu == "🏡 Dashboard":

    st.title("📊 SMART RETAIL INVENTORY ANALYTICS")

    # ── KPI METRICS ──
    total_products   = df["Product Name"].nunique()
    total_transactions = len(df)
    total_stock      = inventory_df["Current Stock"].sum()
    restock_count    = len(
        inventory_df[inventory_df["Stock Status"] == "Restock Needed"]
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Products",  total_products)
    with col2:
        st.metric("Transactions",    total_transactions)
    with col3:
        st.metric("Total Stock",     total_stock)
    with col4:
        st.metric("Need Restock",    restock_count)

    st.divider()

    # ── MODEL ──
    fast_moving      = analytics.get_fast_moving_products()
    restock_products = inventory.get_restock_products()

    # ── PIE CHART CATEGORY ──
    st.subheader("Product Category Distribution")
    category_count = df["Retail Category"].value_counts().reset_index()
    category_count.columns = ["Category", "Count"]

    fig_pie = px.pie(
        category_count,
        names="Category",
        values="Count",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Greens
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # ── BAR CHART FAST MOVING ──
    st.subheader("Top Fast Moving Products")
    fig_bar = px.bar(
        fast_moving,
        x="Product Name",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Greens"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ── DAILY SALES TREND ──
    st.subheader("Daily Transaction Trend")
    daily_sales = (
        df.groupby("Date")["Total Amount"]
        .sum()
        .reset_index()
    )
    fig_line = px.line(
        daily_sales,
        x="Date",
        y="Total Amount",
        color_discrete_sequence=["#16a34a"]
    )
    st.plotly_chart(fig_line, use_container_width=True)

    # ── RESTOCK TABLE ──
    st.subheader("Restock Recommendation")
    if len(restock_products) == 0:

        st.success(
            "✅ All products are currently above minimum stock levels."
        )

    else:
         for _, row in restock_products.iterrows():
            current_stock = row["Current Stock"]
            minimum_stock = row["Minimum Stock"]

        
        # STOCK STATUS
       

            if current_stock <= minimum_stock * 0.5:
                bg_color = "#fee2e2"
                border_color = "#dc2626"
                status = "🔴 CRITICAL STOCK"

            elif current_stock <= minimum_stock:
                bg_color = "#fef3c7"
                border_color = "#f59e0b"
                status = "🟠 LOW STOCK"

            else:
                bg_color = "#dcfce7"
                border_color = "#16a34a"

                status = "🟢 HEALTHY"

            need_stock = (
                minimum_stock
                - current_stock
            )

            st.markdown(
                f"""
                <div style="
                    background:{bg_color};
                    padding:20px;
                    border-radius:15px;
                    margin-bottom:15px;
                    border-left:8px solid {border_color};
                ">

                <h4>{row['Product Name']}</h4>

                <p><b>Status :</b> {status}</p>

                <p><b>Current Stock :</b> {current_stock}</p>

                <p><b>Minimum Stock :</b> {minimum_stock}</p>

                <p><b>Recommended Restock :</b> {need_stock} units</p>

                </div>
                """,
                unsafe_allow_html=True
            )


# HALAMAN ANALYTICS


elif menu == "📈 Analytics":

    st.title("📈 Product Performance & Demand Analysis")

   
    # FEATURE ENGINEERING
    

    features_df = clustering.perform_clustering()

    st.subheader("📊 Product Performance Analysis")

    fig = px.scatter(
        features_df,
        x="Average Daily Sales",
        y="Total Sold",
        text="Product Name",
        size="Total Sold",
        color="Total Sold",
        color_continuous_scale="Greens"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.divider()

    st.subheader("Average Daily Sales")

    average_sales = (
        analytics
        .get_average_daily_sales()
        .reset_index()
    )

    fig_avg = px.bar(
        average_sales.head(10),
        x="Product Name",
        y="Quantity",
        color_discrete_sequence=["#16a34a"]
    )

    st.plotly_chart(
        fig_avg,
        use_container_width=True
    )

    st.divider()

    # =========================
    # INTERACTIVE PRODUCT CHECK
    # =========================

    st.subheader("Check Product Category")

    selected_product = st.selectbox(
        "Choose Product",
        features_df["Product Name"]
    )

    product_data = features_df[
        features_df["Product Name"] == selected_product
    ]

    total_sold = int(
        product_data["Total Sold"].values[0]
    )

    average_sales = round(
        float(product_data["Average Daily Sales"].values[0]),
        2
    )
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Sold",
            total_sold
        )

    with col2:
        st.metric(
            "Estimated Daily Demand",
            f"{round(average_sales)} pcs/day"
        )

    # SIMPLE CLUSTERING RESULT

    cluster = int(
        product_data["Cluster"].values[0]
    )

    if cluster == 1:

        st.success(
            "FAST MOVING PRODUCT"
        )

    else:

        st.warning(
            "SLOW MOVING PRODUCT"
        )

