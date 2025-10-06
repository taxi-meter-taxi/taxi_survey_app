import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import uuid
import os
import shutil

# ファイルパス
CSV_FILE = "responses.csv"
BACKUP_FILE = "responses_backup.csv"

# データ読み込み
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=[
            "ID", "顧客名", "都道府県","販売店名", "担当者名",
            "LTEの提案", "LTEの提案コメント",
            "LTEのコスト感", "LTEのコスト感コメント",
            "ネット解析の評価", "ネット解析の評価コメント",
            "ネット解析のコスト感", "ネット解析のコスト感コメント",
            "売上を上げたい事業者か？", "売上コメント",
            "分析ツールを使っているか？", "分析ツールコメント",
            "複数拠点・車庫が離れている", "複数拠点コメント",
            "無線の使用率", "無線コメント",
            "インバウンド顧客が多いか？", "インバウンドコメント",
            "流しか付け待ちどちらが多いか？", "流しコメント",
            "乗務員の新規採用は多いか？", "採用コメント",
            "解析ソフト・地図ソフト購入不要",
            "カードレス",
            "自動日報", "自動日報コメント",
            "データバックアップ",
            "コールセンター",
            "OTA",
            "料金改定",
            "リアルタイム分析",
            "動態管理",
            "乗降地分析",
            "ドラサポ",
            "乗務員比較",
            "複数拠点情報管理",
            "本社集約",
            "遠隔地でのデータ確認",
            "自由記入欄"
        ])

# データ保存（バックアップ付き）
def save_data(df):
    if os.path.exists(CSV_FILE):
        shutil.copy(CSV_FILE, BACKUP_FILE)
    df.to_csv(CSV_FILE, index=False)

# 回答削除
def delete_entry(df, entry_id):
    df = df[df["ID"] != entry_id]
    save_data(df)
    return df

# グラフ表示
def plot_distribution(column, title):
    if column in data.columns and not data[column].dropna().empty:
        counts = data[column].value_counts()
        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values)
        ax.set_title(title)
        st.pyplot(fig)
    else:
        st.info(f"{title} のデータがありません。")

# アプリ開始
st.title("顧客ヒアリングアンケート管理")

data = load_data()

mode = st.radio("操作モードを選択", ["新規回答", "既存回答の編集・削除"])

if mode == "新規回答":
    st.header("新規回答の追加")
    with st.form("new_entry"):
        new_id = str(uuid.uuid4())[:8]
        name = st.text_input("顧客名")
        prefecture = st.text_input("都道府県")
        store = st.text_input("販売店名")
        staff = st.text_input("担当者名")

        st.subheader("1. 必須")
        q1 = st.radio("①LTEの提案", ["未確認", "〇 良い", "× 悪い"])
        q1_comment = st.text_input("LTEの提案コメント")

        q2 = st.radio("②LTEのコスト感", ["未確認", "〇 安い", "△ 良い", "× 高い"])
        q2_comment = st.text_input("LTEのコスト感コメント（目標価格、要望）")

        q3 = st.radio("③ネット解析の評価", ["未確認", "〇 良い", "× 悪い"])
        q3_comment = st.text_input("ネット解析の評価コメント")

        q4 = st.radio("④ネット解析のコスト感", ["未確認", "〇 安い", "△ 良い", "× 高い"])
        q4_comment = st.text_input("ネット解析のコスト感コメント（目標価格、要望）")

        q5 = st.radio("⑤売上を上げたい事業者か？", ["未確認", "〇 はい", "× いいえ"])
        q5_comment = st.text_input("売上コメント")

        q6 = st.radio("⑥分析ツールを使っているか？", ["未確認", "〇 はい", "× いいえ"])
        q6_comment = st.text_input("分析ツールコメント（使っているツール名）")

        q7 = st.radio("⑦複数拠点、車庫が離れている", ["未確認", "〇 はい", "× いいえ"])
        q7_comment = st.text_input("複数拠点コメント")

        q8 = st.radio("⑧無線の使用率", ["未確認", "〇 高い", "× 低い"])
        q8_comment = st.text_input("無線コメント（比率など）")

        st.subheader("2. 必須ではない")
        q9 = st.radio("①インバウンド顧客が多いか？", ["未確認", "〇 多い", "× 少ない"])
        q9_comment = st.text_input("インバウンドコメント")

        q10 = st.radio("②流しか付け待ちどちらが多いか？", ["未確認", "流し", "付け待ち"])
        q10_comment = st.text_input("流しコメント")

        q11 = st.radio("③乗務員の新規採用は多いか？", ["未確認", "〇 多い", "× 少ない"])
        q11_comment = st.text_input("採用コメント")

        st.subheader("3. 機能について")
        q12 = st.radio("①解析ソフト・地図ソフト購入不要", ["－", "〇", "×"])
        q13 = st.radio("②カードレス", ["－", "〇", "×"])
        q14 = st.radio("③自動日報", ["－", "〇", "×"])
        q14_comment = st.text_input("自動日報コメント（なぜ自動日報をしたいのか？）")
        q15 = st.radio("④データバックアップ", ["－", "〇", "×"])
        q16 = st.radio("⑤コールセンター", ["－", "〇", "×"])
        q17 = st.radio("⑥OTA", ["－", "〇", "×"])
        q18 = st.radio("⑦料金改定", ["－", "〇", "×"])
        q19 = st.radio("⑧リアルタイム分析", ["－", "〇", "×"])
        q20 = st.radio("⑨動態管理", ["－", "〇", "×"])
        q21 = st.radio("⑩乗降地分析", ["－", "〇", "×"])
        q22 = st.radio("⑪ドラサポ", ["－", "〇", "×"])
        q23 = st.radio("⑫乗務員比較", ["－", "〇", "×"])
        q24 = st.radio("⑬複数拠点情報管理", ["－", "〇", "×"])
        q25 = st.radio("⑭本社集約", ["－", "〇", "×"])
        q26 = st.radio("⑮遠隔地でのデータ確認", ["－", "〇", "×"])

        memo = st.text_area("自由記入欄")

        submitted = st.form_submit_button("送信")
        if submitted:
            new_row = pd.DataFrame([{
                "ID": new_id,
                "顧客名": name,
                "都道府県": prefecture,
                "販売店名": store,
                "担当者名": staff,
                "LTEの提案": q1,
                "LTEの提案コメント": q1_comment,
                "LTEのコスト感": q2,
                "LTEのコスト感コメント": q2_comment,
                "ネット解析の評価": q3,
                "ネット解析の評価コメント": q3_comment,
                "ネット解析のコスト感": q4,
                "ネット解析のコスト感コメント": q4_comment,
                "売上を上げたい事業者か？": q5,
                "売上コメント": q5_comment,
                "分析ツールを使っているか？": q6,
                "分析ツールコメント": q6_comment,
                "複数拠点・車庫が離れている": q7,
                "複数拠点コメント": q7_comment,
                "無線の使用率": q8,
                "無線コメント": q8_comment,
                "インバウンド顧客が多いか？": q9,
                "インバウンドコメント": q9_comment,
                "流しか付け待ちどちらが多いか？": q10,
                "流しコメント": q10_comment,
                "乗務員の新規採用は多いか？": q11,
                "採用コメント": q11_comment,
                "解析ソフト・地図ソフト購入不要": q12,
                "カードレス": q13,
                "自動日報": q14,
                "自動日報コメント": q14_comment,
                "データバックアップ": q15,
                "コールセンター": q16,
                "OTA": q17,
                "料金改定": q18,
                "リアルタイム分析": q19,
                "動態管理": q20,
                "乗降地分析": q21,
                "ドラサポ": q22,
                "乗務員比較": q23,
                "複数拠点情報管理": q24,
                "本社集約": q25,
                "遠隔地でのデータ確認": q26,
                "自由記入欄": memo
            }])
            data = pd.concat([data, new_row], ignore_index=True)
            save_data(data)
            st.success("回答を保存しました。")

# 認証処理（管理者のみ回答一覧・CSV・グラフを表示）
ADMIN_PASSWORD = "admin"  # 必要に応じて変更

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    password = st.text_input("管理者パスワードを入力してください", type="password")
    if password == ADMIN_PASSWORD:
        st.session_state["authenticated"] = True
        st.success("認証に成功しました。管理者機能が表示されます。")
    elif password:
        st.error("パスワードが違います。")
    st.stop()

elif mode == "既存回答の編集・削除":
    st.header("既存回答の編集・削除")
    search_name = st.text_input("検索：顧客名")
    search_pref = st.text_input("検索：都道府県")

    filtered = data.copy()
    if search_name:
        filtered = filtered[filtered["顧客名"].str.contains(search_name, na=False)]
    if search_pref:
        filtered = filtered[filtered["都道府県"].str.contains(search_pref, na=False)]

    edit_id = st.selectbox("編集する回答IDを選択", filtered["ID"].tolist())

    if edit_id:
        entry = data[data["ID"] == edit_id].iloc[0]
        with st.form("edit_entry"):
            name = st.text_input("顧客名", value=entry["顧客名"])
            prefecture = st.text_input("都道府県", value=entry["都道府県"])
            store = st.text_input("販売店名", value=entry["販売店名"])
            staff = st.text_input("担当者名", value=entry["担当者名"])

            q1 = st.radio("①LTEの提案", ["未確認", "〇 良い", "× 悪い"], index=["未確認", "〇 良い", "× 悪い"].index(entry["LTEの提案"]))
            q1_comment = st.text_input("LTEの提案コメント", value=entry["LTEの提案コメント"])
            q2 = st.radio("②LTEのコスト感", ["未確認", "〇 安い", "△ 良い", "× 高い"], index=["未確認", "〇 安い", "△ 良い", "× 高い"].index(entry["LTEのコスト感"]))
            q2_comment = st.text_input("LTEのコスト感コメント（目標価格、要望）", value=entry["LTEのコスト感コメント"])
            q3 = st.radio("③ネット解析の評価", ["未確認", "〇 良い", "× 悪い"], index=["未確認", "〇 良い", "× 悪い"].index(entry["ネット解析の評価"]))
            q3_comment = st.text_input("ネット解析の評価コメント", value=entry["ネット解析の評価コメント"])
            q4 = st.radio("④ネット解析のコスト感", ["未確認", "〇 安い", "△ 良い", "× 高い"], index=["未確認", "〇 安い", "△ 良い", "× 高い"].index(entry["ネット解析のコスト感"]))
            q4_comment = st.text_input("ネット解析のコスト感コメント（目標価格、要望）", value=entry["ネット解析のコスト感コメント"])
            q5 = st.radio("⑤売上を上げたい事業者か？", ["未確認", "〇 はい", "× いいえ"], index=["未確認", "〇 はい", "× いいえ"].index(entry["売上を上げたい事業者か？"]))
            q5_comment = st.text_input("売上コメント", value=entry["売上コメント"])
            q6 = st.radio("⑥分析ツールを使っているか？", ["未確認", "〇 はい", "× いいえ"], index=["未確認", "〇 はい", "× いいえ"].index(entry["分析ツールを使っているか？"]))
            q6_comment = st.text_input("分析ツールコメント（使っているツール名）", value=entry["分析ツールコメント"])
            q7 = st.radio("⑦複数拠点、車庫が離れている", ["未確認", "〇 はい", "× いいえ"], index=["未確認", "〇 はい", "× いいえ"].index(entry["複数拠点・車庫が離れている"]))
            q7_comment = st.text_input("複数拠点コメント", value=entry["複数拠点コメント"])
            q8 = st.radio("⑧無線の使用率", ["未確認", "〇 高い", "× 低い"], index=["未確認", "〇 高い", "× 低い"].index(entry["無線の使用率"]))
            q8_comment = st.text_input("無線コメント（比率など）", value=entry["無線コメント"])
            q9 = st.radio("①インバウンド顧客が多いか？", ["未確認", "〇 多い", "× 少ない"], index=["未確認", "〇 多い", "× 少ない"].index(entry["インバウンド顧客が多いか？"]))
            q9_comment = st.text_input("インバウンドコメント", value=entry["インバウンドコメント"])
            q10 = st.radio("②流しか付け待ちどちらが多いか？", ["未確認", "流し", "付け待ち"], index=["未確認", "流し", "付け待ち"].index(entry["流しか付け待ちどちらが多いか？"]))
            q10_comment = st.text_input("流しコメント", value=entry["流しコメント"])
            q11 = st.radio("③乗務員の新規採用は多いか？", ["未確認", "〇 多い", "× 少ない"], index=["未確認", "〇 多い", "× 少ない"].index(entry["乗務員の新規採用は多いか？"]))
            q11_comment = st.text_input("採用コメント", value=entry["採用コメント"])
            q12 = st.radio("①解析ソフト・地図ソフト購入不要", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["解析ソフト・地図ソフト購入不要"]))
            q13 = st.radio("②カードレス", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["カードレス"]))
            q14 = st.radio("③自動日報", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["自動日報"]))
            q14_comment = st.text_input("自動日報コメント（なぜ自動日報をしたいのか？）", value=entry["自動日報コメント"])
            q15 = st.radio("④データバックアップ", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["データバックアップ"]))
            q16 = st.radio("⑤コールセンター", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["コールセンター"]))
            q17 = st.radio("⑥OTA", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["OTA"]))
            q18 = st.radio("⑦料金改定", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["料金改定"]))
            q19 = st.radio("⑧リアルタイム分析", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["リアルタイム分析"]))
            q20 = st.radio("⑨動態管理", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["動態管理"]))
            q21 = st.radio("⑩乗降地分析", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["乗降地分析"]))
            q22 = st.radio("⑪ドラサポ", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["ドラサポ"]))
            q23 = st.radio("⑫乗務員比較", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["乗務員比較"]))
            q24 = st.radio("⑬複数拠点情報管理", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["複数拠点情報管理"]))
            q25 = st.radio("⑭本社集約", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["本社集約"]))
            q26 = st.radio("⑮遠隔地でのデータ確認", ["－", "〇", "×"], index=["－", "〇", "×"].index(entry["遠隔地でのデータ確認"]))
            memo = st.text_area("自由記入欄", value=entry["自由記入欄"])

            updated = st.form_submit_button("修正を保存")
            if updated:
                data.loc[data["ID"] == edit_id] = [
                    edit_id, name, prefecture,
                    q1, q1_comment, q2, q2_comment, q3, q3_comment, q4, q4_comment,
                    q5, q5_comment, q6, q6_comment, q7, q7_comment, q8, q8_comment,
                    q9, q9_comment, q10, q10_comment, q11, q11_comment,
                    q12, q13, q14, q14_comment, q15, q16, q17, q18, q19, q20,
                    q21, q22, q23, q24, q25, q26, memo
                ]
                save_data(data)
                st.success("回答を更新しました。")

        if st.button("この回答を削除"):
            data = delete_entry(data, edit_id)
            st.success(f"回答ID {edit_id} を削除しました。")

# 回答一覧表示
st.header("回答一覧")
st.dataframe(data)

# CSVダウンロード
st.header("CSVファイルのダウンロード")
if not data.empty:
    csv = data.to_csv(index=False).encode("utf-8")
    st.download_button("responses.csv をダウンロード", csv, "responses.csv", "text/csv")

# グラフ表示
st.header("回答傾向のグラフ")
plot_distribution("LTEの提案", "LTEの提案の分布")
plot_distribution("LTEのコスト感", "LTEのコスト感の分布")
plot_distribution("ネット解析の評価", "ネット解析の評価の分布")
plot_distribution("ネット解析のコスト感", "ネット解析のコスト感の分布")
plot_distribution("売上を上げたい事業者か？", "売上を上げたい事業者か？の分布")
plot_distribution("分析ツールを使っているか？", "分析ツールの使用状況")
plot_distribution("複数拠点・車庫が離れている", "複数拠点・車庫が離れているか？の分布")
plot_distribution("無線の使用率", "無線の使用率の分布")
plot_distribution("インバウンド顧客が多いか？", "インバウンド顧客の分布")
plot_distribution("流しか付け待ちどちらが多いか？", "流しか付け待ちの傾向")
plot_distribution("乗務員の新規採用は多いか？", "乗務員の新規採用の分布")
plot_distribution("解析ソフト・地図ソフト購入不要", "解析ソフト・地図ソフト購入不要の分布")
plot_distribution("カードレス", "カードレスの分布")
plot_distribution("自動日報", "自動日報の分布")
plot_distribution("データバックアップ", "データバックアップの分布")
plot_distribution("コールセンター", "コールセンターの分布")
plot_distribution("OTA", "OTAの分布")
plot_distribution("料金改定", "料金改定の分布")
plot_distribution("リアルタイム分析", "リアルタイム分析の分布")
plot_distribution("動態管理", "動態管理の分布")
plot_distribution("乗降地分析", "乗降地分析の分布")
plot_distribution("ドラサポ", "ドラサポの分布")
plot_distribution("乗務員比較", "乗務員比較の分布")
plot_distribution("複数拠点情報管理", "複数拠点情報管理の分布")
plot_distribution("本社集約", "本社集約の分布")
plot_distribution("遠隔地でのデータ確認", "遠隔地でのデータ確認の分布")