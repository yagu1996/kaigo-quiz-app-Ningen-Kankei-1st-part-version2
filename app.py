import streamlit as st
import datetime

# ページ基本設定
st.set_page_config(
    page_title="人間関係とコミュニケーション a前半 練習問題70選",
    page_icon="📝",
    layout="centered"
)

# 明朝体および見やすいレイアウト用カスタムCSS
st.markdown("""
<style>
  /* 全体の背景と基本文字色を強制的に固定（ダークモード干渉を防止） */
  .stApp {
    background-color: #f8fafc !important; /* 明るい清潔な背景色 */
    color: #111827 !important; /* 極濃テキスト */
  }

  /* フォント指定：明朝体 */
  * {
    font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS Mincho", "Source Han Serif", serif !important;
  }

  /* 一般テキスト、見出し、ラジオボタンの文字色をくっきり黒に固定 */
  h1, h2, h3, h4, p, span, label, div {
    color: #0f172a !important;
  }

  /* ルビ（ふりがな）の視認性向上 */
  ruby {
    ruby-align: center;
    color: #000000 !important;
    font-weight: 500;
  }
  rt {
    font-size: 0.65em !important; /* 少し大きくして潰れを防止 */
    font-weight: bold !important;  /* 細くかすれないよう太字化 */
    color: #1e3a8a !important;    /* ふりがなを視認しやすい濃紺色に設定 */
    line-height: 1.2 !important;
  }

  /* 学生情報入力ボックス */
  .student-box {
    background-color: #ffffff !important;
    border: 2px solid #475569 !important;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  /* ナビゲーションボックス */
  .nav-box {
    background-color: #ffffff !important;
    border: 2px solid #64748b !important;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 18px;
  }

  /* 問題カード：白背景にくっきりした濃色の枠線 */
  .q-card {
    background-color: #ffffff !important;
    border: 1.5px solid #64748b !important; /* 枠線を濃くして境界を明瞭化 */
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 16px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
  }

  /* 問題文タイトル：純黒・太字 */
  .q-title {
    font-size: 1.05rem !important;
    font-weight: bold !important;
    margin-bottom: 10px;
    color: #000000 !important;
    line-height: 1.7;
  }

  /* 選択肢テキスト：視認性の高い濃色 */
  .opt-item {
    margin-left: 18px;
    font-size: 0.96rem !important;
    margin-bottom: 6px;
    line-height: 1.6;
    color: #111827 !important;
    font-weight: 500;
  }

  /* 入力欄（テキスト入力・ラジオボタン）自体の文字色も強制黒化 */
  .stTextInput input {
    color: #000000 !important;
    background-color: #ffffff !important;
    border: 1.5px solid #64748b !important;
  }
  
  /* ラジオボタン選択肢の文字 */
  div[role="radiogroup"] label p {
    color: #000000 !important;
    font-size: 1rem !important;
    font-weight: bold !important;
  }

  /* 採点バナー */
  .score-badge {
    text-align: center;
    background-color: #e0f2fe !important;
    border: 2px solid #0284c7 !important;
    border-radius: 8px;
    padding: 18px;
    margin: 20px 0;
  }
</style>
""", unsafe_allow_html=True)

# アプリヘッダー
st.markdown("""
<h2 style='text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px; color: #1e3a8a;'>
<ruby>人間関係<rt>にんげんかんけい</rt></ruby>とコミュニケーション a<ruby>前半<rt>ぜんはん</rt></ruby>
</h2>
<p style='text-align: center; font-size: 0.92rem; color: #475569;'>
練習問題アプリ（全70問・全漢字ルビ付き）｜テキストファイル提出＆コピーペースト提出対応
</p>
""", unsafe_allow_html=True)

# 1. 提出用 学生情報入力欄（最上部に設置）
st.markdown("<div class='student-box'>", unsafe_allow_html=True)
st.markdown("### 👤 学生情報の入力（提出必須）")
col1, col2, col3 = st.columns([1, 1.2, 1.5])
with col1:
    s_class = st.text_input("クラス名（組）", placeholder='例"25B"')
with col2:
    s_id = st.text_input("学籍番号", placeholder='例"9259999"')
with col3:
    s_name = st.text_input("名前（ニックネーム）", placeholder='例"Your nickname"')
st.markdown("</div>", unsafe_allow_html=True)

# 全70問のデータ（全漢字ルビ付き）
QUESTIONS = [
  {
    "id": 1,
    "stem": "<ruby>人類<rt>じんるい</rt></ruby>の<ruby>進化<rt>しんか</rt></ruby>において、チンパンジーとの<ruby>共通祖先<rt>きょうつうそせん</rt></ruby>から<ruby>枝分かれ<rt>えだわかれ</rt></ruby>し、<ruby>直立二足歩行<rt>ちょくりつにそくほこう</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めた<ruby>時期<rt>じき</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>約<rt>やく</rt></ruby>700<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>300<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>100<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>20<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>人類<rt>じんるい</rt></ruby>は<ruby>約<rt>やく</rt></ruby>700<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>に<ruby>共通祖先<rt>きょうつうそせん</rt></ruby>から<ruby>枝分かれ<rt>えだわかれ</rt></ruby>し、<ruby>二足歩行<rt>にそくほこう</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めて<ruby>家族<rt>かぞく</rt></ruby>や<ruby>集団<rt>しゅうだん</rt></ruby>を<ruby>形成<rt>けいせい</rt></ruby>して<ruby>生<rt>せい</rt></ruby>き<ruby>延<rt>の</rt></ruby>びてきました。"
  },
  {
    "id": 2,
    "stem": "<ruby>初期猿人<rt>しょきえんじん</rt></ruby>から<ruby>猿人<rt>えんじん</rt></ruby>への<ruby>進化<rt>しんか</rt></ruby><ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>において、<ruby>約<rt>やく</rt></ruby>400<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby>〜300<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>に<ruby>生息<rt>せいそく</rt></ruby>していた<ruby>代表的<rt>だいひょうてき</rt></ruby>な<ruby>猿人<rt>えんじん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "サヘラントロプス",
      "アウストラロピテクス・アファレンシス",
      "ホモ・エレクトス",
      "ネアンデルタール<ruby>人<rt>じん</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>約<rt>やく</rt></ruby>400<ruby>万<rt>まん</rt></ruby>〜300<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>にはアウストラロピテクス・アファレンシスなどの<ruby>猿人<rt>えんじん</rt></ruby>が<ruby>生息<rt>せいそく</rt></ruby>していました。"
  },
  {
    "id": 3,
    "stem": "ジョージアのドマニシ<ruby>遺跡<rt>いせき</rt></ruby>で<ruby>発<rt>はつ</rt></ruby><ruby>見<rt>み</rt></ruby>された<ruby>約<rt>やく</rt></ruby>180<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>の<ruby>化石<rt>かせき</rt></ruby>から、<ruby>高齢者<rt>こうれいしゃ</rt></ruby>への<ruby>介護<rt>かいご</rt></ruby>が<ruby>行<rt>こう</rt></ruby>われていたことが<ruby>示<rt>し</rt></ruby><ruby>唆<rt>さ</rt></ruby>された<ruby>原人<rt>げんじん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "ホモ・ハビリス",
      "ホモ・エレクトス",
      "ホモ・サピエンス",
      "アウストラロピテクス"
    ],
    "answer": 2,
    "exp": "ドマニシ<ruby>遺跡<rt>いせき</rt></ruby>で<ruby>発<rt>はつ</rt></ruby><ruby>見<rt>み</rt></ruby>された<ruby>歯<rt>は</rt></ruby>のない<ruby>頭蓋骨<rt>とうがいこつ</rt></ruby>の<ruby>化石<rt>かせき</rt></ruby>から、ホモ・エレクトスが<ruby>年<rt>ねん</rt></ruby><ruby>老<rt>ろう</rt></ruby>いた<ruby>仲<rt>なか</rt></ruby><ruby>間<rt>あいだ</rt></ruby>を<ruby>介護<rt>かいご</rt></ruby>していたことが<ruby>推<rt>すい</rt></ruby><ruby>測<rt>そく</rt></ruby>されています。"
  },
  {
    "id": 4,
    "stem": "ドマニシ<ruby>遺跡<rt>いせき</rt></ruby>のホモ・エレクトスの<ruby>頭蓋骨<rt>とうがいこつ</rt></ruby><ruby>化石<rt>かせき</rt></ruby>において、<ruby>仲<rt>なか</rt></ruby><ruby>間<rt>あいだ</rt></ruby>による<ruby>介護<rt>かいご</rt></ruby>が<ruby>行<rt>こう</rt></ruby>われていたと<ruby>判断<rt>はんだん</rt></ruby>された<ruby>根拠<rt>こんきょ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>手<rt>て</rt></ruby><ruby>足<rt>あし</rt></ruby>の<ruby>骨<rt>ほね</rt></ruby><ruby>折<rt>お</rt></ruby>が<ruby>完治<rt>かんち</rt></ruby>していた<ruby>痕跡<rt>こんせき</rt></ruby>",
      "<ruby>歯<rt>は</rt></ruby>がまったくなくなった<ruby>後<rt>あと</rt></ruby>も<ruby>数<rt>かず</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>間<rt>あいだ</rt></ruby><ruby>生存<rt>せいぞん</rt></ruby>していた<ruby>事実<rt>じじつ</rt></ruby>",
      "<ruby>装飾品<rt>そうしょくひん</rt></ruby>を<ruby>身<rt>み</rt></ruby>につけて<ruby>埋葬<rt>まいそう</rt></ruby>されていた<ruby>事実<rt>じじつ</rt></ruby>",
      "<ruby>文字<rt>もじ</rt></ruby>で<ruby>記<rt>き</rt></ruby><ruby>録<rt>ろく</rt></ruby>された<ruby>石<rt>いし</rt></ruby><ruby>板<rt>いた</rt></ruby>が<ruby>副<rt>ふく</rt></ruby><ruby>葬<rt>そう</rt></ruby>されていた<ruby>事実<rt>じじつ</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>加<rt>か</rt></ruby><ruby>齢<rt>れい</rt></ruby>で<ruby>歯<rt>は</rt></ruby>がなくなった<ruby>後<rt>あと</rt></ruby>も<ruby>数<rt>かず</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>間<rt>あいだ</rt></ruby><ruby>生<rt>せい</rt></ruby>きていたことから、<ruby>仲<rt>なか</rt></ruby><ruby>間<rt>あいだ</rt></ruby>が<ruby>柔<rt>じゅう</rt></ruby>らかくした<ruby>食<rt>しょく</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>を<ruby>与<rt>あた</rt></ruby>えるなどの<ruby>世<rt>せ</rt></ruby><ruby>話<rt>はな</rt></ruby>をしていたと<ruby>考<rt>かんが</rt></ruby>えられています。"
  },
  {
    "id": 5,
    "stem": "<ruby>約<rt>やく</rt></ruby>70<ruby>万<rt>まん</rt></ruby>〜20<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>に<ruby>生息<rt>せいそく</rt></ruby>し、スペインの<ruby>遺跡<rt>いせき</rt></ruby><ruby>等<rt>とう</rt></ruby>で<ruby>死者<rt>ししゃ</rt></ruby>を「<ruby>埋葬<rt>まいそう</rt></ruby>」した<ruby>痕跡<rt>こんせき</rt></ruby>が<ruby>確<rt>かく</rt></ruby><ruby>認<rt>にん</rt></ruby>されている<ruby>人類<rt>じんるい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "アルディピテクス",
      "ホモ・ハイデルベルゲンシス",
      "パラントロプス",
      "ホモ・フローレシエンシス"
    ],
    "answer": 2,
    "exp": "ホモ・ハイデルベルゲンシスには<ruby>埋葬<rt>まいそう</rt></ruby>の<ruby>痕跡<rt>こんせき</rt></ruby>があり、「<ruby>死<rt>し</rt></ruby>」や「<ruby>時<rt>とき</rt></ruby><ruby>間<rt>あいだ</rt></ruby>」などの<ruby>抽象的思考<rt>ちゅうしょうてきしこう</rt></ruby>の<ruby>芽<rt>め</rt></ruby><ruby>生<rt>せい</rt></ruby>えが<ruby>示<rt>し</rt></ruby><ruby>唆<rt>さ</rt></ruby>されています。"
  },
  {
    "id": 6,
    "stem": "ホモ・ハイデルベルゲンシスによる<ruby>埋葬<rt>まいそう</rt></ruby>の<ruby>痕跡<rt>こんせき</rt></ruby>から<ruby>推<rt>すい</rt></ruby><ruby>測<rt>そく</rt></ruby>される<ruby>能力<rt>のうりょく</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>農耕<rt>のうこう</rt></ruby>と<ruby>灌漑技術<rt>かんがいぎじゅつ</rt></ruby>の<ruby>確立<rt>かくりつ</rt></ruby>",
      "「<ruby>死<rt>し</rt></ruby>」や「<ruby>時<rt>とき</rt></ruby><ruby>間<rt>あいだ</rt></ruby>」といった<ruby>抽象的思考<rt>ちゅうしょうてきしこう</rt></ruby>や<ruby>言語<rt>げんご</rt></ruby>の<ruby>使用<rt>しよう</rt></ruby>",
      "<ruby>青銅器<rt>せいどうき</rt></ruby>や<ruby>鉄器<rt>てっき</rt></ruby>の<ruby>製造技術<rt>せいぞうぎじゅつ</rt></ruby>",
      "<ruby>国家組織<rt>こっかそしき</rt></ruby>による<ruby>福祉制度<rt>ふくしせいど</rt></ruby>の<ruby>制定<rt>せいてい</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>埋葬<rt>まいそう</rt></ruby><ruby>行為<rt>こうい</rt></ruby>は<ruby>死者<rt>ししゃ</rt></ruby>への<ruby>配慮<rt>はいりょ</rt></ruby>だけでなく、<ruby>目<rt>め</rt></ruby>に<ruby>見<rt>み</rt></ruby>えない「<ruby>死<rt>し</rt></ruby>」や「<ruby>時<rt>とき</rt></ruby><ruby>間<rt>あいだ</rt></ruby>」を<ruby>捉<rt>とら</rt></ruby>える<ruby>抽象的思考<rt>ちゅうしょうてきしこう</rt></ruby>や<ruby>知性<rt>ちせい</rt></ruby>の<ruby>発達<rt>はったつ</rt></ruby>を<ruby>示<rt>し</rt></ruby>しています。"
  },
  {
    "id": 7,
    "stem": "<ruby>現代<rt>げんだい</rt></ruby>の<ruby>私<rt>わたし</rt></ruby>たちに<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby>つながる「<ruby>新人<rt>しんじん</rt></ruby>（ホモ・サピエンス）」がアフリカで<ruby>誕生<rt>たんじょう</rt></ruby>した<ruby>時期<rt>じき</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>約<rt>やく</rt></ruby>700<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>180<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>20<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>",
      "<ruby>約<rt>やく</rt></ruby>1<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>"
    ],
    "answer": 3,
    "exp": "<ruby>現代<rt>げんだい</rt></ruby><ruby>人<rt>ひと</rt></ruby>（ホモ・サピエンス）は<ruby>約<rt>やく</rt></ruby>20<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>にアフリカで<ruby>誕生<rt>たんじょう</rt></ruby>したとされています。"
  },
  {
    "id": 8,
    "stem": "ホモ・サピエンスが<ruby>約<rt>やく</rt></ruby>7<ruby>万<rt>まん</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>前<rt>まえ</rt></ruby>から<ruby>獲得<rt>かくとく</rt></ruby>し、<ruby>大<rt>おお</rt></ruby>きな<ruby>集団<rt>しゅうだん</rt></ruby>での<ruby>情報共有<rt>じょうほうきょうゆう</rt></ruby>や<ruby>強固<rt>きょうこ</rt></ruby>な<ruby>絆<rt>きずな</rt></ruby>を<ruby>可<rt>か</rt></ruby><ruby>能<rt>のう</rt></ruby>にした<ruby>能力<rt>のうりょく</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>文字<rt>もじ</rt></ruby>による<ruby>法<rt>ほう</rt></ruby><ruby>典<rt>てん</rt></ruby>の<ruby>制定<rt>せいてい</rt></ruby>",
      "<ruby>柔軟<rt>じゅうなん</rt></ruby>な<ruby>言語<rt>げんご</rt></ruby><ruby>能力<rt>のうりょく</rt></ruby>と、<ruby>現実<rt>げんじつ</rt></ruby>にはない<ruby>世<rt>せ</rt></ruby><ruby>界<rt>かい</rt></ruby>を<ruby>思<rt>おも</rt></ruby>い<ruby>描<rt>えが</rt></ruby>く<ruby>想像力<rt>そうぞうりょく</rt></ruby>（<ruby>物語<rt>ものがたり</rt></ruby>の<ruby>共有<rt>きょうゆう</rt></ruby>）",
      "<ruby>金<rt>きん</rt></ruby><ruby>属<rt>ぞく</rt></ruby><ruby>器<rt>き</rt></ruby>を<ruby>用<rt>よう</rt></ruby>いた<ruby>大<rt>おお</rt></ruby><ruby>規<rt>き</rt></ruby><ruby>模<rt>も</rt></ruby>な<ruby>狩<rt>しゅ</rt></ruby><ruby>猟<rt>りょう</rt></ruby>",
      "<ruby>家族<rt>かぞく</rt></ruby>を<ruby>解<rt>かい</rt></ruby><ruby>体<rt>たい</rt></ruby>して<ruby>個<rt>こ</rt></ruby>々<ruby>人<rt>ひと</rt></ruby>で<ruby>自<rt>じ</rt></ruby><ruby>活<rt>かつ</rt></ruby>する<ruby>生活様式<rt>せいかつようしき</rt></ruby>"
    ],
    "answer": 2,
    "exp": "ホモ・サピエンスは<ruby>言語<rt>げんご</rt></ruby>と<ruby>想像力<rt>そうぞうりょく</rt></ruby>によって「<ruby>物語<rt>ものがたり</rt></ruby>」をつくり<ruby>共有<rt>きょうゆう</rt></ruby>し、<ruby>数<rt>かず</rt></ruby><ruby>多<rt>おお</rt></ruby>くの<ruby>人間<rt>にんげん</rt></ruby>が<ruby>協<rt>きょう</rt></ruby><ruby>力<rt>ちから</rt></ruby>し<ruby>合<rt>あ</rt></ruby>う<ruby>大<rt>おお</rt></ruby>きな<ruby>共同体<rt>きょうどうたい</rt></ruby>や<ruby>宗教<rt>しゅうきょう</rt></ruby>を<ruby>生<rt>せい</rt></ruby>み<ruby>出<rt>で</rt></ruby>しました。"
  },
  {
    "id": 9,
    "stem": "<ruby>人類<rt>じんるい</rt></ruby>の「<ruby>直立二足歩行<rt>ちょくりつにそくほこう</rt></ruby>」に<ruby>伴<rt>ともな</rt></ruby>い<ruby>骨盤<rt>こつばん</rt></ruby>の<ruby>形状<rt>けいじょう</rt></ruby>が<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>したことで<ruby>生<rt>せい</rt></ruby>じた、<ruby>乳児<rt>にゅうじ</rt></ruby>の<ruby>発達<rt>はったつ</rt></ruby><ruby>上<rt>うえ</rt></ruby>の<ruby>特徴<rt>とくちょう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>生<rt>せい</rt></ruby>まれた<ruby>直<rt>ちょく</rt></ruby><ruby>後<rt>あと</rt></ruby>から<ruby>自力<rt>じりき</rt></ruby>で<ruby>歩行<rt>ほこう</rt></ruby>できる",
      "<ruby>産道<rt>さんどう</rt></ruby>が<ruby>狭<rt>せま</rt></ruby>くなったため、<ruby>極めて<rt>きわめて</rt></ruby><ruby>未熟<rt>みじゅく</rt></ruby>な<ruby>状態<rt>じょうたい</rt></ruby>で<ruby>生<rt>せい</rt></ruby>まれる（<ruby>生理的早産<rt>せいりてきそうざん</rt></ruby>）",
      "<ruby>親<rt>おや</rt></ruby>の<ruby>手助け<rt>てだすけ</rt></ruby>がなくても<ruby>食物<rt>しょくもつ</rt></ruby>を<ruby>摂取<rt>せっしゅ</rt></ruby>できる",
      "<ruby>成育期間<rt>せいいくきかん</rt></ruby>が<ruby>短縮<rt>たんしゅく</rt></ruby>され<ruby>数<rt>かず</rt></ruby>か<ruby>月<rt>つき</rt></ruby>で<ruby>成体<rt>せいたい</rt></ruby>になる"
    ],
    "answer": 2,
    "exp": "<ruby>直立二足歩行<rt>ちょくりつにそくほこう</rt></ruby>によって<ruby>産道<rt>さんどう</rt></ruby>が<ruby>狭<rt>せま</rt></ruby>くなったため、<ruby>人類<rt>じんるい</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>ちゃんは<ruby>極めて<rt>きわめて</rt></ruby><ruby>未熟<rt>みじゅく</rt></ruby>な<ruby>状態<rt>じょうたい</rt></ruby>（<ruby>生理的早産<rt>せいりてきそうざん</rt></ruby>）で<ruby>生<rt>せい</rt></ruby>まれ、<ruby>長<rt>なが</rt></ruby><ruby>期<rt>き</rt></ruby><ruby>間<rt>あいだ</rt></ruby>の<ruby>手<rt>て</rt></ruby><ruby>厚<rt>あつ</rt></ruby>いケアを<ruby>必要<rt>ひつよう</rt></ruby>とします。"
  },
  {
    "id": 10,
    "stem": "<ruby>人類<rt>じんるい</rt></ruby>が<ruby>直立二足歩行<rt>ちょくりつにそくほこう</rt></ruby>と<ruby>生理的早産<rt>せいりてきそうざん</rt></ruby>を<ruby>経<rt>けい</rt></ruby>て<ruby>進化<rt>しんか</rt></ruby>する<ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>で、<ruby>不可欠<rt>ふかけつ</rt></ruby>となった<ruby>生活様式<rt>せいかつようしき</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>単<rt>たん</rt></ruby><ruby>独<rt>どく</rt></ruby><ruby>行<rt>こう</rt></ruby><ruby>動<rt>どう</rt></ruby>による<ruby>生存競争<rt>せいぞんきょうそう</rt></ruby>の<ruby>徹<rt>てつ</rt></ruby><ruby>底<rt>そこ</rt></ruby>",
      "<ruby>一夫一婦制<rt>いっぷいっぷせい</rt></ruby>による<ruby>家族<rt>かぞく</rt></ruby>の<ruby>形成<rt>けいせい</rt></ruby>や、<ruby>共同<rt>きょうどう</rt></ruby>での<ruby>子育て<rt>こそだて</rt></ruby>・ケアの<ruby>営み<rt>いとなみ</rt></ruby>",
      "<ruby>移動<rt>いどう</rt></ruby>をやめて<ruby>単<rt>たん</rt></ruby><ruby>独<rt>どく</rt></ruby>で<ruby>洞窟<rt>どうくつ</rt></ruby>に<ruby>孤立<rt>こりつ</rt></ruby>すること",
      "<ruby>老<rt>ろう</rt></ruby><ruby>齢<rt>れい</rt></ruby><ruby>者<rt>しゃ</rt></ruby>や<ruby>病<rt>びょう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>を<ruby>即<rt>そく</rt></ruby><ruby>座<rt>ざ</rt></ruby>に<ruby>集団<rt>しゅうだん</rt></ruby>から<ruby>排除<rt>はいじょ</rt></ruby>すること"
    ],
    "answer": 2,
    "exp": "<ruby>未熟<rt>みじゅく</rt></ruby>な<ruby>子<rt>こ</rt></ruby>どもを<ruby>育<rt>いく</rt></ruby>てるため、<ruby>一夫一婦制<rt>いっぷいっぷせい</rt></ruby>による<ruby>家族<rt>かぞく</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>や、<ruby>集団<rt>しゅうだん</rt></ruby>で<ruby>協<rt>きょう</rt></ruby><ruby>力<rt>ちから</rt></ruby>して<ruby>助<rt>じょ</rt></ruby>け<ruby>合<rt>あ</rt></ruby>う「ケア（<ruby>介護<rt>かいご</rt></ruby>）」の<ruby>営み<rt>いとなみ</rt></ruby>が<ruby>進化<rt>しんか</rt></ruby><ruby>上<rt>うえ</rt></ruby><ruby>不可欠<rt>ふかけつ</rt></ruby>となりました。"
  },
  {
    "id": 11,
    "stem": "<ruby>教科書<rt>きょうかしょ</rt></ruby>において、「<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>思いやり<rt>おもいやり</rt></ruby>、<ruby>介護<rt>かいご</rt></ruby>を<ruby>行<rt>こう</rt></ruby>うこと」について<ruby>述<rt>じゅつ</rt></ruby>べた<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>他<rt>た</rt></ruby>の<ruby>動物界<rt>どうぶつかい</rt></ruby>でも<ruby>普遍的<rt>ふへんてき</rt></ruby>にみられる<ruby>日常的行動<rt>にちじょうてきこうどう</rt></ruby>である",
      "<ruby>人類<rt>じんるい</rt></ruby>の<ruby>進化<rt>しんか</rt></ruby>の<ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>で<ruby>獲得<rt>かくとく</rt></ruby>された、<ruby>人間<rt>にんげん</rt></ruby>らしさの<ruby>象徴<rt>しょうちょう</rt></ruby>である",
      "<ruby>文明<rt>ぶんめい</rt></ruby>が<ruby>発達<rt>はったつ</rt></ruby>した<ruby>近代以降<rt>きんだいいこう</rt></ruby>に<ruby>初<rt>しょ</rt></ruby>めて<ruby>生<rt>せい</rt></ruby>まれた<ruby>人工的<rt>じんこうてき</rt></ruby>な<ruby>制<rt>せい</rt></ruby><ruby>度<rt>ど</rt></ruby>である",
      "<ruby>本<rt>ほん</rt></ruby><ruby>来<rt>く</rt></ruby>の<ruby>人間<rt>にんげん</rt></ruby>の<ruby>本能<rt>ほんのう</rt></ruby>に<ruby>反<rt>はん</rt></ruby>する<ruby>不自然<rt>ふしぜん</rt></ruby>な<ruby>行為<rt>こうい</rt></ruby>である"
    ],
    "answer": 2,
    "exp": "<ruby>介護<rt>かいご</rt></ruby>を<ruby>行<rt>こう</rt></ruby>うことは<ruby>動物界<rt>どうぶつかい</rt></ruby>では<ruby>極めて<rt>きわめて</rt></ruby><ruby>珍<rt>めずら</rt></ruby>しく、<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>思いやり<rt>おもいやり</rt></ruby><ruby>協<rt>きょう</rt></ruby><ruby>力<rt>ちから</rt></ruby>して<ruby>生<rt>せい</rt></ruby>き<ruby>延<rt>の</rt></ruby>びてきた「<ruby>人間<rt>にんげん</rt></ruby>らしさの<ruby>象徴<rt>しょうちょう</rt></ruby>」とされています。"
  },
  {
    "id": 12,
    "stem": "<ruby>介護福祉職<rt>かいごふくししょく</rt></ruby>が「<ruby>人類<rt>じんるい</rt></ruby><ruby>進化<rt>しんか</rt></ruby>の<ruby>歴<rt>れき</rt></ruby><ruby>史<rt>し</rt></ruby>における<ruby>介護<rt>かいご</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>」を<ruby>学<rt>がく</rt></ruby>ぶ<ruby>意義<rt>いぎ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>単<rt>たん</rt></ruby>なる<ruby>身体介助作業<rt>しんたいかいじょさぎょう</rt></ruby>としてではなく、<ruby>人間<rt>にんげん</rt></ruby>らしい<ruby>営み<rt>いとなみ</rt></ruby>を<ruby>支<rt>し</rt></ruby>える<ruby>専門職<rt>せんもんしょく</rt></ruby>としての<ruby>誇り<rt>ほこり</rt></ruby>と<ruby>自覚<rt>じかく</rt></ruby>をもつため",
      "<ruby>太<rt>ふと</rt></ruby><ruby>古<rt>ふる</rt></ruby>の<ruby>狩猟技術<rt>しゅりょうぎじゅつ</rt></ruby>を<ruby>実<rt>じつ</rt></ruby><ruby>際<rt>さい</rt></ruby>の<ruby>介護<rt>かいご</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>場<rt>ば</rt></ruby>で<ruby>再現<rt>さいげん</rt></ruby>するため",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>自立<rt>じりつ</rt></ruby>を<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>して<ruby>全面的<rt>ぜんめんてき</rt></ruby>に<ruby>依存<rt>いぞん</rt></ruby>させるため",
      "<ruby>介護保険制度<rt>かいごほけんせいど</rt></ruby>の<ruby>財源<rt>ざいげん</rt></ruby>を<ruby>削減<rt>さくげん</rt></ruby>する<ruby>論理<rt>ろんり</rt></ruby>を<ruby>身<rt>み</rt></ruby>につけるため"
    ],
    "answer": 1,
    "exp": "<ruby>人類<rt>じんるい</rt></ruby>が<ruby>培<rt>ばい</rt></ruby>ってきた「<ruby>他者<rt>たしゃ</rt></ruby>をケアする<ruby>悠<rt>ゆう</rt></ruby><ruby>久<rt>ひさ</rt></ruby>の<ruby>歴<rt>れき</rt></ruby><ruby>史<rt>し</rt></ruby>」を<ruby>理解<rt>りかい</rt></ruby>することは、<ruby>介護福祉士<rt>かいごふくしし</rt></ruby>が<ruby>誇り<rt>ほこり</rt></ruby>と<ruby>高<rt>たか</rt></ruby>い<ruby>専<rt>せん</rt></ruby><ruby>門<rt>もん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>自覚<rt>じかく</rt></ruby>をもって<ruby>支援<rt>しえん</rt></ruby>にあたる<ruby>基<rt>き</rt></ruby><ruby>盤<rt>ばん</rt></ruby>となります。"
  },
  {
    "id": 13,
    "stem": "<ruby>自分<rt>じぶん</rt></ruby>という<ruby>存<rt>ぞん</rt></ruby><ruby>在<rt>ざい</rt></ruby>を<ruby>形<rt>かたち</rt></ruby>づくる「<ruby>先天的要素<rt>せんてんてきようそ</rt></ruby>」の<ruby>説<rt>せつ</rt></ruby><ruby>明<rt>あか</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>生<rt>せい</rt></ruby>まれた<ruby>国<rt>くに</rt></ruby>の<ruby>言語<rt>げんご</rt></ruby>や<ruby>文<rt>ぶん</rt></ruby><ruby>化<rt>か</rt></ruby>を<ruby>学<rt>がく</rt></ruby><ruby>習<rt>しゅう</rt></ruby>すること",
      "<ruby>両<rt>りょう</rt></ruby><ruby>親<rt>おや</rt></ruby>や<ruby>過<rt>か</rt></ruby><ruby>去<rt>きょ</rt></ruby>の<ruby>人類<rt>じんるい</rt></ruby>から<ruby>受<rt>う</rt></ruby>け<ruby>継<rt>つ</rt></ruby>いだ<ruby>遺伝子<rt>いでんし</rt></ruby>による<ruby>生物学的設計図<rt>せいぶつがくてきせっけいず</rt></ruby>",
      "<ruby>学校教育<rt>がっこうきょういく</rt></ruby>や<ruby>職場<rt>しょくば</rt></ruby>での<ruby>人間関係<rt>にんげんかんけい</rt></ruby>から<ruby>得<rt>え</rt></ruby>た<ruby>知識<rt>ちしき</rt></ruby>",
      "<ruby>生活環境<rt>せいかつかんきょう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>培<rt>ばい</rt></ruby>われた<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>道徳的信条<rt>どうとくてきしんじょう</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>先天的要素<rt>せんてんてきようそ</rt></ruby>とは、<ruby>両<rt>りょう</rt></ruby><ruby>親<rt>おや</rt></ruby>や<ruby>先<rt>さき</rt></ruby><ruby>祖<rt>そ</rt></ruby>から<ruby>受<rt>う</rt></ruby>け<ruby>継<rt>つ</rt></ruby>いだ<ruby>遺伝子<rt>いでんし</rt></ruby>（<ruby>体<rt>たい</rt></ruby><ruby>型<rt>がた</rt></ruby>や<ruby>肌<rt>はだ</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>などを<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>づける<ruby>生物学的設計図<rt>せいぶつがくてきせっけいず</rt></ruby>）を<ruby>指<rt>ゆび</rt></ruby>します。"
  },
  {
    "id": 14,
    "stem": "<ruby>自分<rt>じぶん</rt></ruby>という<ruby>存<rt>ぞん</rt></ruby><ruby>在<rt>ざい</rt></ruby>を<ruby>形<rt>かたち</rt></ruby>づくる「<ruby>後天的要素<rt>こうてんてきようそ</rt></ruby>」の<ruby>説<rt>せつ</rt></ruby><ruby>明<rt>あか</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>遺伝情報<rt>いでんじょうほう</rt></ruby>によって<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>される<ruby>血液型<rt>けつえきがた</rt></ruby>",
      "<ruby>生活環境<rt>せいかつかんきょう</rt></ruby>、<ruby>人<rt>ひと</rt></ruby>との<ruby>ふれあい<rt>ふれあい</rt></ruby>、<ruby>経験<rt>けいけん</rt></ruby>を<ruby>通<rt>つう</rt></ruby>じて<ruby>積<rt>つ</rt></ruby>み<ruby>上<rt>うえ</rt></ruby>げられる<ruby>知識<rt>ちしき</rt></ruby>や<ruby>価値観<rt>かちかん</rt></ruby>",
      "<ruby>受精時<rt>じゅせいじ</rt></ruby>に<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>される<ruby>先天的<rt>せんてんてき</rt></ruby>な<ruby>染色体構造<rt>せんしょくたいこうぞう</rt></ruby>",
      "<ruby>生<rt>せい</rt></ruby><ruby>物<rt>もの</rt></ruby><ruby>学<rt>がく</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>骨格<rt>こっかく</rt></ruby>や<ruby>網膜<rt>もうまく</rt></ruby>の<ruby>構造<rt>こうぞう</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>後天的要素<rt>こうてんてきようそ</rt></ruby>とは、<ruby>自<rt>じ</rt></ruby><ruby>然<rt>ぜん</rt></ruby>・<ruby>物<rt>もの</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>環境<rt>かんきょう</rt></ruby>や<ruby>人<rt>ひと</rt></ruby>との<ruby>出<rt>で</rt></ruby><ruby>会<rt>かい</rt></ruby>い、<ruby>経験<rt>けいけん</rt></ruby>を<ruby>通<rt>つう</rt></ruby>じて<ruby>形成<rt>けいせい</rt></ruby>される<ruby>知識<rt>ちしき</rt></ruby>・<ruby>能力<rt>のうりょく</rt></ruby>・<ruby>価値観<rt>かちかん</rt></ruby>などのことです。"
  },
  {
    "id": 15,
    "stem": "<ruby>言語<rt>げんご</rt></ruby>の<ruby>獲得<rt>かくとく</rt></ruby>に<ruby>関<rt>かん</rt></ruby>して、<ruby>先天的要素<rt>せんてんてきようそ</rt></ruby>と<ruby>後天的要素<rt>こうてんてきようそ</rt></ruby>の<ruby>関係<rt>かんけい</rt></ruby>を<ruby>述<rt>じゅつ</rt></ruby>べた<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>言語<rt>げんご</rt></ruby>（<ruby>日<rt>ひ</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>語<rt>ご</rt></ruby>など）を<ruby>話<rt>はな</rt></ruby>す<ruby>知識<rt>ちしき</rt></ruby>そのものが<ruby>遺伝子<rt>いでんし</rt></ruby>に<ruby>組<rt>くみ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>まれている",
      "<ruby>言語<rt>げんご</rt></ruby>を<ruby>獲得<rt>かくとく</rt></ruby>する<ruby>脳<rt>のう</rt></ruby>の<ruby>柔軟<rt>じゅうなん</rt></ruby>な<ruby>能力<rt>のうりょく</rt></ruby>は<ruby>先天的<rt>せんてんてき</rt></ruby>に<ruby>備<rt>そな</rt></ruby>わり、どの<ruby>言語<rt>げんご</rt></ruby>を<ruby>話<rt>はな</rt></ruby>すかは<ruby>後天的<rt>こうてんてき</rt></ruby>な<ruby>環境<rt>かんきょう</rt></ruby>によって<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>される",
      "<ruby>言語<rt>げんご</rt></ruby>の<ruby>習<rt>しゅう</rt></ruby><ruby>得<rt>え</rt></ruby>には<ruby>先天的要素<rt>せんてんてきようそ</rt></ruby>は<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>与<rt>あた</rt></ruby>せず、<ruby>環境<rt>かんきょう</rt></ruby>だけで<ruby>決<rt>けつ</rt></ruby>まる",
      "<ruby>後天的要素<rt>こうてんてきようそ</rt></ruby>は<ruby>言語獲得<rt>げんごかくとく</rt></ruby>に<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>せず、すべて<ruby>遺伝子<rt>いでんし</rt></ruby>で<ruby>決<rt>けつ</rt></ruby>まる"
    ],
    "answer": 2,
    "exp": "<ruby>言語<rt>げんご</rt></ruby>を<ruby>獲得<rt>かくとく</rt></ruby>する<ruby>能力<rt>のうりょく</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>体<rt>たい</rt></ruby>は<ruby>遺伝子<rt>いでんし</rt></ruby>に<ruby>組<rt>くみ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>まれていますが、<ruby>実<rt>じつ</rt></ruby><ruby>際<rt>さい</rt></ruby>にどの<ruby>言語<rt>げんご</rt></ruby>を<ruby>話<rt>はな</rt></ruby>すかは<ruby>育<rt>いく</rt></ruby>った<ruby>環境<rt>かんきょう</rt></ruby>（<ruby>後天的要素<rt>こうてんてきようそ</rt></ruby>）によって<ruby>決<rt>けつ</rt></ruby>まります。"
  },
  {
    "id": 16,
    "stem": "<ruby>広<rt>ひろ</rt></ruby><ruby>辞<rt>じ</rt></ruby><ruby>苑<rt>えん</rt></ruby><ruby>等<rt>とう</rt></ruby>で「<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>・<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>・<ruby>意<rt>い</rt></ruby><ruby>志<rt>し</rt></ruby>・<ruby>行為<rt>こうい</rt></ruby>の<ruby>主体<rt>しゅたい</rt></ruby>としての<ruby>私<rt>わたし</rt></ruby>」と<ruby>定<rt>てい</rt></ruby><ruby>義<rt>ぎ</rt></ruby>される<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自我<rt>じが</rt></ruby>",
      "<ruby>適応動作<rt>てきおうどうさ</rt></ruby>",
      "<ruby>防衛機制<rt>ぼうえいきせい</rt></ruby>",
      "<ruby>ステレオタイプ<rt>すてれおたいぷ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>自我<rt>じが</rt></ruby>とは、<ruby>外界<rt>がいかい</rt></ruby>の<ruby>対象<rt>たいしょう</rt></ruby>や<ruby>他者<rt>たしゃ</rt></ruby>と<ruby>区<rt>く</rt></ruby><ruby>別<rt>べつ</rt></ruby>された「<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>・<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>・<ruby>意<rt>い</rt></ruby><ruby>志<rt>し</rt></ruby>・<ruby>行為<rt>こうい</rt></ruby>の<ruby>主体<rt>しゅたい</rt></ruby>としての<ruby>私<rt>わたし</rt></ruby>」を<ruby>自覚<rt>じかく</rt></ruby>する<ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>のことです。"
  },
  {
    "id": 17,
    "stem": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>成<rt>せい</rt></ruby><ruby>長<rt>なが</rt></ruby><ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>において「<ruby>自我の芽生え<rt>じがのめばえ</rt></ruby>」が<ruby>起<rt>お</rt></ruby>きることの<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>他者<rt>たしゃ</rt></ruby>との<ruby>身体的接触<rt>しんたいてきせっしょく</rt></ruby>が<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>不<rt>ふ</rt></ruby><ruby>要<rt>よう</rt></ruby>になること",
      "<ruby>自分<rt>じぶん</rt></ruby>が<ruby>自分<rt>じぶん</rt></ruby>であり、<ruby>他者<rt>たしゃ</rt></ruby>とは<ruby>異<rt>い</rt></ruby>なる<ruby>別<rt>べつ</rt></ruby><ruby>個<rt>こ</rt></ruby>の<ruby>人格<rt>じんかく</rt></ruby>であると<ruby>自覚<rt>じかく</rt></ruby>し<ruby>始<rt>はじ</rt></ruby>めること",
      "<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>と<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>同一化<rt>どういつか</rt></ruby>すること",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>のルールや<ruby>法規範<rt>ほうきはん</rt></ruby>をすべて<ruby>理解<rt>りかい</rt></ruby>し<ruby>遵守<rt>じゅんしゅ</rt></ruby>できるようになること"
    ],
    "answer": 2,
    "exp": "<ruby>成<rt>せい</rt></ruby><ruby>長<rt>なが</rt></ruby>に<ruby>伴<rt>ともな</rt></ruby>い、<ruby>自分<rt>じぶん</rt></ruby>と<ruby>他者<rt>たしゃ</rt></ruby>との<ruby>違<rt>ちが</rt></ruby>いを<ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>し、「<ruby>私<rt>わたし</rt></ruby>は<ruby>他<rt>た</rt></ruby>のだれでもない<ruby>私<rt>わたし</rt></ruby>である」という<ruby>主体<rt>しゅたい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>をもつことが<ruby>自我の芽生え<rt>じがのめばえ</rt></ruby>です。"
  },
  {
    "id": 18,
    "stem": "<ruby>人間<rt>にんげん</rt></ruby>の「<ruby>内面<rt>ないめん</rt></ruby>」を<ruby>理解<rt>りかい</rt></ruby>することの<ruby>難<rt>むずか</rt></ruby>しさについて<ruby>述<rt>じゅつ</rt></ruby>べた<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>内面<rt>ないめん</rt></ruby>は<ruby>外<rt>そと</rt></ruby><ruby>見<rt>み</rt></ruby>の<ruby>動作<rt>どうさ</rt></ruby>を<ruby>見<rt>み</rt></ruby>れば<ruby>誰<rt>だれ</rt></ruby>でも100%<ruby>正<rt>せい</rt></ruby><ruby>確<rt>かく</rt></ruby>に<ruby>把<rt>は</rt></ruby><ruby>握<rt>にぎ</rt></ruby>できる",
      "<ruby>内面<rt>ないめん</rt></ruby>には<ruby>潜在意識<rt>せんざいいしき</rt></ruby>や<ruby>無意識<rt>むいしき</rt></ruby>の<ruby>領域<rt>りょういき</rt></ruby>があり、<ruby>内省<rt>ないせい</rt></ruby>してもすべてを<ruby>捉<rt>とら</rt></ruby>えることは<ruby>困<rt>こま</rt></ruby><ruby>難<rt>むずか</rt></ruby>である",
      "<ruby>内面<rt>ないめん</rt></ruby>は<ruby>年齢<rt>ねんれい</rt></ruby>とともに<ruby>固定化<rt>こていか</rt></ruby>し、<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>しなくなるため<ruby>理解<rt>りかい</rt></ruby>しやすい",
      "<ruby>心<rt>こころ</rt></ruby><ruby>理<rt>り</rt></ruby>テストを1<ruby>回<rt>かい</rt></ruby><ruby>行<rt>こう</rt></ruby>えばその<ruby>人<rt>ひと</rt></ruby>の<ruby>内面<rt>ないめん</rt></ruby>のすべてが<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>数<rt>かず</rt></ruby><ruby>値<rt>ね</rt></ruby><ruby>化<rt>か</rt></ruby>される"
    ],
    "answer": 2,
    "exp": "<ruby>人<rt>ひと</rt></ruby>の<ruby>内面<rt>ないめん</rt></ruby>には<ruby>自分<rt>じぶん</rt></ruby>でも<ruby>自覚<rt>じかく</rt></ruby>していない<ruby>無意識<rt>むいしき</rt></ruby>や<ruby>潜在意識<rt>せんざいいしき</rt></ruby>が<ruby>存<rt>ぞん</rt></ruby><ruby>在<rt>ざい</rt></ruby>し、<ruby>絶<rt>ぜつ</rt></ruby>えず<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>しているため、<ruby>内面<rt>ないめん</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>理解<rt>りかい</rt></ruby>することは<ruby>容<rt>よう</rt></ruby><ruby>易<rt>い</rt></ruby>ではありません。"
  },
  {
    "id": 19,
    "stem": "<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>する<ruby>際<rt>さい</rt></ruby>の「<ruby>感覚器<rt>かんかくき</rt></ruby>（<ruby>五感<rt>ごかん</rt></ruby>）」の<ruby>役割<rt>やくわり</rt></ruby>と<ruby>限界<rt>げんかい</rt></ruby>について<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>視覚<rt>しかく</rt></ruby>や<ruby>聴覚<rt>ちょうかく</rt></ruby>で<ruby>得<rt>え</rt></ruby>た<ruby>情報<rt>じょうほう</rt></ruby>だけで、<ruby>相手<rt>あいて</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>思<rt>おも</rt></ruby>いのすべてを<ruby>深<rt>ふか</rt></ruby>く<ruby>理解<rt>りかい</rt></ruby>できる",
      "<ruby>視覚<rt>しかく</rt></ruby>・<ruby>聴覚<rt>ちょうかく</rt></ruby>などの<ruby>情報<rt>じょうほう</rt></ruby>をもとに<ruby>脳<rt>のう</rt></ruby>で<ruby>処<rt>しょ</rt></ruby><ruby>理<rt>り</rt></ruby>するが、<ruby>目<rt>め</rt></ruby>に<ruby>見<rt>み</rt></ruby>えない<ruby>内面<rt>ないめん</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>には<ruby>届<rt>とど</rt></ruby>かない<ruby>部<rt>ぶ</rt></ruby><ruby>分<rt>ぶん</rt></ruby>がある",
      "<ruby>嗅覚<rt>きゅうかく</rt></ruby>や<ruby>触覚<rt>しょっかく</rt></ruby>は<ruby>対<rt>たい</rt></ruby><ruby>人<rt>ひと</rt></ruby>コミュニケーションにおいては<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>用<rt>よう</rt></ruby>されない",
      "<ruby>感覚器<rt>かんかくき</rt></ruby>から<ruby>得<rt>え</rt></ruby>られる<ruby>情報<rt>じょうほう</rt></ruby>には<ruby>個人的<rt>こじんてき</rt></ruby>な<ruby>主観<rt>しゅかん</rt></ruby>やバイアスは<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>入<rt>はい</rt></ruby>り<ruby>込<rt>こ</rt></ruby>まない"
    ],
    "answer": 2,
    "exp": "<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>は<ruby>感覚器<rt>かんかくき</rt></ruby>（<ruby>視覚<rt>しかく</rt></ruby>・<ruby>聴覚<rt>ちょうかく</rt></ruby><ruby>等<rt>とう</rt></ruby>）からの<ruby>情報<rt>じょうほう</rt></ruby>から<ruby>始<rt>はじ</rt></ruby>まりますが、<ruby>相手<rt>あいて</rt></ruby>の<ruby>内面<rt>ないめん</rt></ruby>にある<ruby>目<rt>め</rt></ruby>に<ruby>見<rt>み</rt></ruby>えない<ruby>思<rt>おも</rt></ruby>いまでは<ruby>捉<rt>とら</rt></ruby>えきれない<ruby>限界<rt>げんかい</rt></ruby>があります。"
  },
  {
    "id": 20,
    "stem": "<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>する<ruby>際<rt>さい</rt></ruby>、<ruby>人間<rt>にんげん</rt></ruby>が<ruby>無意識<rt>むいしき</rt></ruby>のうちに<ruby>行<rt>こう</rt></ruby>ってしまう<ruby>認知プロセス<rt>にんちぷろせす</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>と<ruby>相手<rt>あいて</rt></ruby>を<ruby>比<rt>ひ</rt></ruby><ruby>較<rt>かく</rt></ruby>し、<ruby>共通点<rt>きょうつうてん</rt></ruby>や<ruby>相違点<rt>そういてん</rt></ruby>を<ruby>探<rt>さが</rt></ruby>そうとする",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>らず、<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>遮断<rt>しゃだん</rt></ruby>する",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>脳<rt>のう</rt></ruby>の<ruby>思考回路<rt>しこうかいろ</rt></ruby>を<ruby>物<rt>もの</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby>スキャンする",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>過<rt>か</rt></ruby><ruby>去<rt>きょ</rt></ruby>の<ruby>全<rt>ぜん</rt></ruby><ruby>記<rt>き</rt></ruby><ruby>憶<rt>おく</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>復<rt>ふく</rt></ruby><ruby>元<rt>もと</rt></ruby>して<ruby>共有<rt>きょうゆう</rt></ruby>する"
    ],
    "answer": 1,
    "exp": "<ruby>私<rt>わたし</rt></ruby>たちは<ruby>無意識<rt>むいしき</rt></ruby>のうちに<ruby>自分<rt>じぶん</rt></ruby>と<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>比<rt>ひ</rt></ruby>べ、どこが<ruby>同<rt>おな</rt></ruby>じでどこが<ruby>違<rt>ちが</rt></ruby>うのかを<ruby>照<rt>しょう</rt></ruby>らし<ruby>合<rt>あ</rt></ruby>わせながら<ruby>相手<rt>あいて</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>しようとします。"
  },
  {
    "id": 21,
    "stem": "「<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>した」と<ruby>考<rt>かんが</rt></ruby>える<ruby>際<rt>さい</rt></ruby>に、<ruby>対人援助職<rt>たいじんえんじょしょく</rt></ruby>が<ruby>常<rt>じょう</rt></ruby>に<ruby>心<rt>こころ</rt></ruby>に<ruby>留<rt>りゅう</rt></ruby>めておくべき<ruby>姿勢<rt>しせい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "「<ruby>自分<rt>じぶん</rt></ruby>は<ruby>相手<rt>あいて</rt></ruby>のすべてを<ruby>客観的<rt>きゃっかんてき</rt></ruby>・<ruby>完<rt>かん</rt></ruby><ruby>璧<rt>ぺき</rt></ruby>に<ruby>理解<rt>りかい</rt></ruby>した」と<ruby>確信<rt>かくしん</rt></ruby>すること",
      "「<ruby>自分<rt>じぶん</rt></ruby>が<ruby>理解<rt>りかい</rt></ruby>した<ruby>内<rt>うち</rt></ruby><ruby>容<rt>よう</rt></ruby>は、あくまで<ruby>自分流<rt>じぶんりゅう</rt></ruby>のフィルターを<ruby>通<rt>つう</rt></ruby>した<ruby>他者<rt>たしゃ</rt></ruby><ruby>理解<rt>りかい</rt></ruby>である」と<ruby>自覚<rt>じかく</rt></ruby>すること",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>言<rt>げん</rt></ruby>った<ruby>言葉<rt>ことば</rt></ruby>の<ruby>表<rt>ひょう</rt></ruby><ruby>面<rt>めん</rt></ruby>だけを<ruby>鵜<rt>う</rt></ruby><ruby>呑<rt>の</rt></ruby>みにして<ruby>疑<rt>ぎ</rt></ruby>わないこと",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>理解<rt>りかい</rt></ruby>を<ruby>諦<rt>あきら</rt></ruby>め、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>常識<rt>じょうしき</rt></ruby>や<ruby>経験則<rt>けいけんそく</rt></ruby>だけに<ruby>基<rt>き</rt></ruby>づいて<ruby>指示<rt>しじ</rt></ruby>を<ruby>出<rt>で</rt></ruby>すこと"
    ],
    "answer": 2,
    "exp": "<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>するときは<ruby>常<rt>じょう</rt></ruby>に「<ruby>自分<rt>じぶん</rt></ruby>というフィルター」を<ruby>通<rt>つう</rt></ruby>しているため、「<ruby>自分流<rt>じぶんりゅう</rt></ruby>の<ruby>他者<rt>たしゃ</rt></ruby><ruby>理解<rt>りかい</rt></ruby>にすぎない」と<ruby>自覚<rt>じかく</rt></ruby>することが<ruby>大切<rt>たいせつ</rt></ruby>です。"
  },
  {
    "id": 22,
    "stem": "<ruby>自分<rt>じぶん</rt></ruby>と<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>違<rt>ちが</rt></ruby>いを<ruby>認<rt>にん</rt></ruby><ruby>識<rt>しき</rt></ruby>することと「<ruby>人間の尊厳<rt>にんげんのそんげん</rt></ruby>」の<ruby>関係<rt>かんけい</rt></ruby>について<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>違<rt>ちが</rt></ruby>いを「<ruby>優<rt>ゆう</rt></ruby>れている・<ruby>劣<rt>れつ</rt></ruby>っている」という<ruby>優劣<rt>ゆうれつ</rt></ruby>で<ruby>評価<rt>ひょうか</rt></ruby>すること",
      "<ruby>違<rt>ちが</rt></ruby>いをその<ruby>人<rt>ひと</rt></ruby>の「<ruby>持ち味<rt>もちあじ</rt></ruby>・<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>」として<ruby>認<rt>にん</rt></ruby>め、かけがえのない1<ruby>人<rt>ひと</rt></ruby>の<ruby>人間<rt>にんげん</rt></ruby>として<ruby>尊重<rt>そんちょう</rt></ruby>すること",
      "<ruby>違<rt>ちが</rt></ruby>いをなくすために、<ruby>相手<rt>あいて</rt></ruby>を<ruby>自分<rt>じぶん</rt></ruby>と<ruby>同<rt>おな</rt></ruby>じ<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>に<ruby>矯正<rt>きょうせい</rt></ruby>すること",
      "<ruby>違<rt>ちが</rt></ruby>いがある<ruby>人<rt>ひと</rt></ruby>とは<ruby>関<rt>かん</rt></ruby>わりを<ruby>持<rt>も</rt></ruby>たず、<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>はな</rt></ruby>を<ruby>置<rt>お</rt></ruby>くこと"
    ],
    "answer": 2,
    "exp": "<ruby>他者<rt>たしゃ</rt></ruby>との<ruby>違<rt>ちが</rt></ruby>いを<ruby>優劣<rt>ゆうれつ</rt></ruby>ではなく「<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>」として<ruby>捉<rt>とら</rt></ruby>えることが、<ruby>相手<rt>あいて</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>を<ruby>守<rt>まも</rt></ruby>り、<ruby>同<rt>おな</rt></ruby><ruby>時<rt>とき</rt></ruby>に<ruby>自分<rt>じぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>み</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>をも<ruby>大切<rt>たいせつ</rt></ruby>にすることにつながります。"
  },
  {
    "id": 23,
    "stem": "<ruby>対人援助職<rt>たいじんえんじょしょく</rt></ruby>にとって「<ruby>自己覚知<rt>じこかくち</rt></ruby>」が<ruby>必要<rt>ひつよう</rt></ruby><ruby>不可欠<rt>ふかけつ</rt></ruby>とされる<ruby>理<rt>り</rt></ruby><ruby>由<rt>ゆ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>や<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>の<ruby>偏<rt>へん</rt></ruby>り（バイアス）が<ruby>無意識<rt>むいしき</rt></ruby>に<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>押し付け<rt>おしつけ</rt></ruby>られるのを<ruby>防<rt>ぼう</rt></ruby>ぐため",
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>学歴<rt>がくれき</rt></ruby>や<ruby>経歴<rt>けいれき</rt></ruby>を<ruby>相手<rt>あいて</rt></ruby>に<ruby>誇示<rt>こじ</rt></ruby>して<ruby>主導権<rt>しゅどうけん</rt></ruby>を<ruby>握<rt>にぎ</rt></ruby>るため",
      "<ruby>援助者<rt>えんじょしゃ</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>み</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>消<rt>き</rt></ruby>し<ruby>去<rt>きょ</rt></ruby>り、<ruby>機械<rt>きかい</rt></ruby>のように<ruby>対<rt>たい</rt></ruby><ruby>応<rt>おう</rt></ruby>するため",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>要<rt>よう</rt></ruby><ruby>求<rt>もと</rt></ruby>をすべて<ruby>拒<rt>きょ</rt></ruby><ruby>否<rt>ひ</rt></ruby>する<ruby>論理<rt>ろんり</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>口実<rt>こうじつ</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけるため"
    ],
    "answer": 1,
    "exp": "<ruby>自己覚知<rt>じこかくち</rt></ruby>により<ruby>自<rt>じ</rt></ruby>らの<ruby>価値観<rt>かちかん</rt></ruby>や<ruby>偏<rt>へん</rt></ruby><ruby>見<rt>み</rt></ruby>の<ruby>癖<rt>くせ</rt></ruby>を<ruby>知<rt>ち</rt></ruby>ることで、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>主観<rt>しゅかん</rt></ruby>を<ruby>不<rt>ふ</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>意<rt>い</rt></ruby>に<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>押し付け<rt>おしつけ</rt></ruby>ず、<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>を<ruby>築<rt>ちく</rt></ruby>くことができます。"
  },
  {
    "id": 24,
    "stem": "<ruby>自己覚知<rt>じこかくち</rt></ruby>を<ruby>深<rt>ふか</rt></ruby>めるための<ruby>具<rt>ぐ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>方<rt>かた</rt></ruby><ruby>法<rt>ほう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>行<rt>こう</rt></ruby><ruby>動<rt>どう</rt></ruby>や<ruby>言動<rt>げんどう</rt></ruby>を<ruby>振<rt>ふ</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>る<ruby>内省<rt>ないせい</rt></ruby>や、<ruby>他者<rt>たしゃ</rt></ruby>から<ruby>自分<rt>じぶん</rt></ruby>がどう<ruby>見<rt>み</rt></ruby>えているかの<ruby>確<rt>かく</rt></ruby><ruby>認<rt>にん</rt></ruby>を<ruby>行<rt>こう</rt></ruby>う",
      "<ruby>他者<rt>たしゃ</rt></ruby>からの<ruby>批判<rt>ひはん</rt></ruby>やアドバイスを<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>遮断<rt>しゃだん</rt></ruby>して<ruby>自己主張<rt>じこしゅちょう</rt></ruby>を<ruby>貫く<rt>つらぬく</rt></ruby>",
      "<ruby>心<rt>こころ</rt></ruby><ruby>理<rt>り</rt></ruby>テストの<ruby>結果<rt>けっか</rt></ruby>を<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>し、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>第一印象<rt>だいいちいんしょう</rt></ruby>のみを<ruby>信<rt>しん</rt></ruby>じる",
      "<ruby>過<rt>か</rt></ruby><ruby>去<rt>きょ</rt></ruby>の<ruby>失<rt>しつ</rt></ruby><ruby>敗<rt>はい</rt></ruby>をすべて<ruby>忘<rt>わす</rt></ruby>れ、<ruby>反<rt>はん</rt></ruby><ruby>省<rt>しょう</rt></ruby>することをやめる"
    ],
    "answer": 1,
    "exp": "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby>の<ruby>言動<rt>げんどう</rt></ruby>やこころの<ruby>動<rt>どう</rt></ruby>きを<ruby>注<rt>ちゅう</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>深<rt>ふか</rt></ruby>く<ruby>振<rt>ふ</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>る<ruby>内省<rt>ないせい</rt></ruby>や、<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>かこ</rt></ruby>からの<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>・フィードバックを<ruby>素<rt>そ</rt></ruby><ruby>直<rt>ちょく</rt></ruby>に<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めることで<ruby>自己覚知<rt>じこかくち</rt></ruby>が<ruby>深<rt>ふか</rt></ruby>まります。"
  },
  {
    "id": 25,
    "stem": "「<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>」において、<ruby>人間関係<rt>にんげんかんけい</rt></ruby>の<ruby>内面<rt>ないめん</rt></ruby>を<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>する2つの<ruby>軸<rt>じく</rt></ruby>（<ruby>視点<rt>してん</rt></ruby>）として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>過<rt>か</rt></ruby><ruby>去<rt>きょ</rt></ruby>と<ruby>未<rt>み</rt></ruby><ruby>来<rt>く</rt></ruby>",
      "<ruby>主観的<rt>しゅかんてき</rt></ruby>な<ruby>視点<rt>してん</rt></ruby>（<ruby>自分<rt>じぶん</rt></ruby>が<ruby>知<rt>ち</rt></ruby>っている／<ruby>知<rt>ち</rt></ruby>らない）と<ruby>客観的<rt>きゃっかんてき</rt></ruby>な<ruby>視点<rt>してん</rt></ruby>（<ruby>他者<rt>たしゃ</rt></ruby>が<ruby>知<rt>ち</rt></ruby>っている／<ruby>知<rt>ち</rt></ruby>らない）",
      "<ruby>善悪<rt>ぜんあく</rt></ruby>の<ruby>基準<rt>きじゅん</rt></ruby>と<ruby>損得<rt>そんとく</rt></ruby>の<ruby>基準<rt>きじゅん</rt></ruby>",
      "<ruby>肉体的<rt>にくたいてき</rt></ruby>な<ruby>能力<rt>のうりょく</rt></ruby>と<ruby>精神的<rt>せいしんてき</rt></ruby>な<ruby>能力<rt>のうりょく</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>は、「<ruby>自分<rt>じぶん</rt></ruby>が<ruby>知<rt>ち</rt></ruby>っている／<ruby>知<rt>ち</rt></ruby>らない」と「<ruby>他者<rt>たしゃ</rt></ruby>が<ruby>知<rt>ち</rt></ruby>っている／<ruby>知<rt>ち</rt></ruby>らない」の2<ruby>軸<rt>じく</rt></ruby>で4つの<ruby>領域<rt>りょういき</rt></ruby>（<ruby>窓<rt>まど</rt></ruby>）に<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>します。"
  },
  {
    "id": 26,
    "stem": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>における「<ruby>開放の窓<rt>かいほうのまど</rt></ruby>」の<ruby>定<rt>てい</rt></ruby><ruby>義<rt>ぎ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>も<ruby>知<rt>ち</rt></ruby>っている<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>自分<rt>じぶん</rt></ruby>は<ruby>知<rt>ち</rt></ruby>っているが、<ruby>他者<rt>たしゃ</rt></ruby>は<ruby>知<rt>ち</rt></ruby>らない<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>他者<rt>たしゃ</rt></ruby>は<ruby>知<rt>ち</rt></ruby>っているが、<ruby>自分<rt>じぶん</rt></ruby>は<ruby>知<rt>ち</rt></ruby>らない<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>も<ruby>知<rt>ち</rt></ruby>らない<ruby>領域<rt>りょういき</rt></ruby>"
    ],
    "answer": 1,
    "exp": "「<ruby>開放の窓<rt>かいほうのまど</rt></ruby>」は、<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>も<ruby>共<rt>きょう</rt></ruby>に<ruby>把<rt>は</rt></ruby><ruby>握<rt>にぎ</rt></ruby>・<ruby>共有<rt>きょうゆう</rt></ruby>している<ruby>領域<rt>りょういき</rt></ruby>であり、<ruby>円<rt>えん</rt></ruby><ruby>滑<rt>かつ</rt></ruby>なコミュニケーションの<ruby>基<rt>き</rt></ruby><ruby>礎<rt>そ</rt></ruby>となります。"
  },
  {
    "id": 27,
    "stem": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>における「<ruby>秘密の窓<rt>ひみつのまど</rt></ruby>」の<ruby>定<rt>てい</rt></ruby><ruby>義<rt>ぎ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>も<ruby>知<rt>ち</rt></ruby>っている<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>自分<rt>じぶん</rt></ruby>は<ruby>知<rt>ち</rt></ruby>っているが、<ruby>他者<rt>たしゃ</rt></ruby>には<ruby>知<rt>ち</rt></ruby>らせていない・<ruby>隠<rt>かく</rt></ruby>している<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>他者<rt>たしゃ</rt></ruby>は<ruby>知<rt>ち</rt></ruby>っているが、<ruby>自分<rt>じぶん</rt></ruby>は<ruby>気<rt>き</rt></ruby>づいていない<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>誰<rt>だれ</rt></ruby>も<ruby>気<rt>き</rt></ruby>づいていない<ruby>未<rt>み</rt></ruby><ruby>知<rt>ち</rt></ruby>の<ruby>領域<rt>りょういき</rt></ruby>"
    ],
    "answer": 2,
    "exp": "「<ruby>秘密の窓<rt>ひみつのまど</rt></ruby>」は、<ruby>自分<rt>じぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>み</rt></ruby>は<ruby>分<rt>ぶん</rt></ruby>かっているが、<ruby>他者<rt>たしゃ</rt></ruby>にはあえて<ruby>伝<rt>つた</rt></ruby>えていない、あるいは<ruby>他者<rt>たしゃ</rt></ruby>が<ruby>気<rt>き</rt></ruby>づいていない<ruby>領域<rt>りょういき</rt></ruby>です。"
  },
  {
    "id": 28,
    "stem": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>における「<ruby>盲点の窓<rt>もうてんのまど</rt></ruby>」の<ruby>定<rt>てい</rt></ruby><ruby>義<rt>ぎ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>だけが<ruby>知<rt>ち</rt></ruby>っている<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby>の<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>他者<rt>たしゃ</rt></ruby>は<ruby>知<rt>ち</rt></ruby>っている・<ruby>気<rt>き</rt></ruby>づいているが、<ruby>自分<rt>じぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>み</rt></ruby>は<ruby>気<rt>き</rt></ruby>づいていない<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>もよく<ruby>知<rt>ち</rt></ruby>っているオープンな<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>将<rt>しょう</rt></ruby><ruby>来<rt>く</rt></ruby>にわたって<ruby>絶<rt>ぜつ</rt></ruby><ruby>対<rt>たい</rt></ruby>に<ruby>解<rt>かい</rt></ruby><ruby>明<rt>あか</rt></ruby>されない<ruby>領域<rt>りょういき</rt></ruby>"
    ],
    "answer": 2,
    "exp": "「<ruby>盲点の窓<rt>もうてんのまど</rt></ruby>」は、<ruby>自分<rt>じぶん</rt></ruby>では<ruby>無意識<rt>むいしき</rt></ruby>の<ruby>癖<rt>くせ</rt></ruby>など<ruby>気<rt>き</rt></ruby>づいていないが、<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>かこ</rt></ruby>の<ruby>他者<rt>たしゃ</rt></ruby>からはよく<ruby>見<rt>み</rt></ruby>えている<ruby>領域<rt>りょういき</rt></ruby>を<ruby>指<rt>ゆび</rt></ruby>します。"
  },
  {
    "id": 29,
    "stem": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>における「<ruby>未知の窓<rt>みちのまど</rt></ruby>」の<ruby>定<rt>てい</rt></ruby><ruby>義<rt>ぎ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>もまだ<ruby>気<rt>き</rt></ruby>づいていない、<ruby>潜<rt>せん</rt></ruby><ruby>在<rt>ざい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>可能性<rt>かのうせい</rt></ruby>や<ruby>無意識<rt>むいしき</rt></ruby>の<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>自分<rt>じぶん</rt></ruby>が<ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>隠<rt>かく</rt></ruby>しているプライバシーの<ruby>領域<rt>りょういき</rt></ruby>",
      "<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>かこ</rt></ruby>から<ruby>指<rt>ゆび</rt></ruby><ruby>摘<rt>てき</rt></ruby>されて<ruby>初<rt>しょ</rt></ruby>めて<ruby>自覚<rt>じかく</rt></ruby>した<ruby>領域<rt>りょういき</rt></ruby>",
      "お<ruby>互<rt>たが</rt></ruby>いに<ruby>周<rt>しゅう</rt></ruby><ruby>知<rt>ち</rt></ruby>の<ruby>事実<rt>じじつ</rt></ruby>となっている<ruby>共有<rt>きょうゆう</rt></ruby><ruby>領域<rt>りょういき</rt></ruby>"
    ],
    "answer": 1,
    "exp": "「<ruby>未知の窓<rt>みちのまど</rt></ruby>」は、<ruby>本<rt>ほん</rt></ruby><ruby>人<rt>ひと</rt></ruby>も<ruby>他者<rt>たしゃ</rt></ruby>もまだ<ruby>気<rt>き</rt></ruby>づいていない<ruby>可能性<rt>かのうせい</rt></ruby>や<ruby>潜<rt>せん</rt></ruby><ruby>在<rt>ざい</rt></ruby><ruby>能力<rt>のうりょく</rt></ruby>、<ruby>深<rt>ふか</rt></ruby><ruby>層<rt>そう</rt></ruby><ruby>心<rt>こころ</rt></ruby><ruby>理<rt>り</rt></ruby>の<ruby>領域<rt>りょういき</rt></ruby>です。"
  },
  {
    "id": 30,
    "stem": "<ruby>ジョハリの窓<rt>じょはりのまど</rt></ruby>において、<ruby>他者<rt>たしゃ</rt></ruby>からの<ruby>指<rt>ゆび</rt></ruby><ruby>摘<rt>てき</rt></ruby>やフィードバックを<ruby>吟<rt>ぎん</rt></ruby><ruby>味<rt>あじ</rt></ruby>して<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めたときに<ruby>生<rt>せい</rt></ruby>じる<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>縦<rt>たて</rt></ruby>の<ruby>境界線<rt>きょうかいせん</rt></ruby>が<ruby>右<rt>みぎ</rt></ruby>に<ruby>移動<rt>いどう</rt></ruby>し、「<ruby>盲点の窓<rt>もうてんのまど</rt></ruby>」が<ruby>狭<rt>せま</rt></ruby>くなって「<ruby>開放の窓<rt>かいほうのまど</rt></ruby>」が<ruby>広<rt>ひろ</rt></ruby>がる",
      "<ruby>横<rt>よこ</rt></ruby>の<ruby>境界線<rt>きょうかいせん</rt></ruby>が<ruby>下<rt>した</rt></ruby>に<ruby>移動<rt>いどう</rt></ruby>し、「<ruby>秘密の窓<rt>ひみつのまど</rt></ruby>」が<ruby>広<rt>ひろ</rt></ruby>がる",
      "すべての<ruby>境界線<rt>きょうかいせん</rt></ruby>が<ruby>左<rt>ひだり</rt></ruby><ruby>端<rt>はし</rt></ruby>に<ruby>移動<rt>いどう</rt></ruby>し、「<ruby>開放の窓<rt>かいほうのまど</rt></ruby>」が<ruby>消滅<rt>しょうめつ</rt></ruby>する",
      "「<ruby>未知の窓<rt>みちのまど</rt></ruby>」だけが<ruby>急<rt>きゅう</rt></ruby><ruby>激<rt>げき</rt></ruby>に<ruby>拡大<rt>かくだい</rt></ruby>する"
    ],
    "answer": 1,
    "exp": "<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>評価<rt>ひょうか</rt></ruby>や<ruby>指<rt>ゆび</rt></ruby><ruby>摘<rt>てき</rt></ruby>を<ruby>自分<rt>じぶん</rt></ruby>のなかで<ruby>吟<rt>ぎん</rt></ruby><ruby>味<rt>あじ</rt></ruby>することで、<ruby>気<rt>き</rt></ruby>づかなかった<ruby>盲<rt>もう</rt></ruby><ruby>点<rt>てん</rt></ruby>が<ruby>減<rt>げん</rt></ruby>り（<ruby>盲点の窓<rt>もうてんのまど</rt></ruby>が<ruby>縮<rt>しゅく</rt></ruby><ruby>小<rt>ちい</rt></ruby>）、<ruby>開放の窓<rt>かいほうのまど</rt></ruby>が<ruby>右<rt>みぎ</rt></ruby>へと<ruby>拡大<rt>かくだい</rt></ruby>します。"
  },
  {
    "id": 31,
    "stem": "「<ruby>自分<rt>じぶん</rt></ruby>についての<ruby>盲点の窓<rt>もうてんのまど</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>になくし、<ruby>境界線<rt>きょうかいせん</rt></ruby>を<ruby>右<rt>みぎ</rt></ruby><ruby>端<rt>はし</rt></ruby>まで<ruby>移動<rt>いどう</rt></ruby>させること」について<ruby>教科書<rt>きょうかしょ</rt></ruby>が<ruby>述<rt>じゅつ</rt></ruby>べている<ruby>見<rt>み</rt></ruby><ruby>解<rt>かい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>誰<rt>だれ</rt></ruby>もが<ruby>努<rt>ど</rt></ruby><ruby>力<rt>ちから</rt></ruby><ruby>次<rt>つぎ</rt></ruby><ruby>第<rt>だい</rt></ruby>で<ruby>短期間<rt>たんきかん</rt></ruby>に<ruby>達成<rt>たっせい</rt></ruby>できる",
      "だれもが<ruby>自分<rt>じぶん</rt></ruby>について<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>にすべてを<ruby>知<rt>ち</rt></ruby>ることは<ruby>不<rt>ふ</rt></ruby><ruby>可<rt>か</rt></ruby><ruby>能<rt>のう</rt></ruby>である",
      "<ruby>介護福祉士<rt>かいごふくしし</rt></ruby>になれば<ruby>自<rt>じ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>右<rt>みぎ</rt></ruby><ruby>端<rt>はし</rt></ruby>まで<ruby>到<rt>とう</rt></ruby><ruby>達<rt>たつ</rt></ruby>する",
      "<ruby>盲<rt>もう</rt></ruby><ruby>点<rt>てん</rt></ruby>をなくすことは<ruby>人格<rt>じんかく</rt></ruby>の<ruby>崩壊<rt>ほうかい</rt></ruby>を<ruby>招<rt>まね</rt></ruby>くため<ruby>禁止<rt>きんし</rt></ruby>されている"
    ],
    "answer": 2,
    "exp": "<ruby>教科書<rt>きょうかしょ</rt></ruby>では「<ruby>境界線<rt>きょうかいせん</rt></ruby>が<ruby>右<rt>みぎ</rt></ruby><ruby>端<rt>はし</rt></ruby>まで<ruby>移動<rt>いどう</rt></ruby>することはない、つまりだれもが<ruby>自分<rt>じぶん</rt></ruby>について<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>にすべてを<ruby>知<rt>ち</rt></ruby>ることはできない」と<ruby>指<rt>ゆび</rt></ruby><ruby>摘<rt>てき</rt></ruby>されています。"
  },
  {
    "id": 32,
    "stem": "コミュニケーションを<ruby>通<rt>つう</rt></ruby>じて<ruby>自分<rt>じぶん</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>他者<rt>たしゃ</rt></ruby>に<ruby>提<rt>てい</rt></ruby><ruby>供<rt>きょう</rt></ruby>し、「<ruby>秘密の窓<rt>ひみつのまど</rt></ruby>」を「<ruby>開放の窓<rt>かいほうのまど</rt></ruby>」へと<ruby>広<rt>ひろ</rt></ruby>げていく<ruby>行為<rt>こうい</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶか<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自己主張<rt>じこしゅちょう</rt></ruby>",
      "<ruby>自己開示<rt>じこかいじ</rt></ruby>",
      "<ruby>自己防衛<rt>じこぼうえい</rt></ruby>",
      "<ruby>自己客観化<rt>じこきゃっかんか</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>自分<rt>じぶん</rt></ruby>についての<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>他者<rt>たしゃ</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>える<ruby>行為<rt>こうい</rt></ruby>を「<ruby>自己開示<rt>じこかいじ</rt></ruby>」といい、これにより<ruby>秘密の窓<rt>ひみつのまど</rt></ruby>が<ruby>狭<rt>せま</rt></ruby>まり、<ruby>開放の窓<rt>かいほうのまど</rt></ruby>が<ruby>下<rt>した</rt></ruby>へと<ruby>広<rt>ひろ</rt></ruby>がります。"
  },
  {
    "id": 33,
    "stem": "<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>自己開示<rt>じこかいじ</rt></ruby>を<ruby>行<rt>こう</rt></ruby>うことによって<ruby>人間関係<rt>にんげんかんけい</rt></ruby>にもたらされる<ruby>好影響<rt>こうえいきょう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>相手<rt>あいて</rt></ruby>にも<ruby>自己開示<rt>じこかいじ</rt></ruby>が<ruby>促<rt>うなが</rt></ruby>され（<ruby>返報性<rt>へんぽうせい</rt></ruby>）、<ruby>相互理解<rt>そうごりかい</rt></ruby>と<ruby>親<rt>おや</rt></ruby>しみが<ruby>深<rt>ふか</rt></ruby>まる",
      "<ruby>相手<rt>あいて</rt></ruby>を<ruby>自分<rt>じぶん</rt></ruby>の<ruby>思<rt>おも</rt></ruby>い<ruby>通<rt>つう</rt></ruby>りにコントロールできるようになる",
      "<ruby>自分<rt>じぶん</rt></ruby>のプライバシーを<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>放<rt>ほう</rt></ruby><ruby>棄<rt>き</rt></ruby>して<ruby>相手<rt>あいて</rt></ruby>に<ruby>服従<rt>ふくじゅう</rt></ruby>できる",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby>を<ruby>無<rt>む</rt></ruby><ruby>理<rt>り</rt></ruby>やり<ruby>暴<rt>ぼう</rt></ruby>き<ruby>出<rt>で</rt></ruby>すことができる"
    ],
    "answer": 1,
    "exp": "<ruby>自己開示<rt>じこかいじ</rt></ruby>を<ruby>行<rt>こう</rt></ruby>うと、<ruby>相手<rt>あいて</rt></ruby>も<ruby>安<rt>あん</rt></ruby><ruby>心<rt>こころ</rt></ruby>や<ruby>関<rt>かん</rt></ruby><ruby>心<rt>こころ</rt></ruby>を<ruby>抱<rt>だ</rt></ruby>いて<ruby>自己開示<rt>じこかいじ</rt></ruby>しやすくなり、お<ruby>互<rt>たが</rt></ruby>いの<ruby>理解<rt>りかい</rt></ruby>と<ruby>信頼<rt>しんらい</rt></ruby>が<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>深<rt>ふか</rt></ruby>まっていきます。"
  },
  {
    "id": 34,
    "stem": "<ruby>自己開示<rt>じこかいじ</rt></ruby>を<ruby>活<rt>かつ</rt></ruby><ruby>用<rt>よう</rt></ruby>する<ruby>際<rt>さい</rt></ruby>の<ruby>留意点<rt>りゅういてん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>初対面<rt>しょたいめん</rt></ruby>の<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>で、いきなり<ruby>過<rt>か</rt></ruby><ruby>度<rt>ど</rt></ruby>に<ruby>詳<rt>しょう</rt></ruby><ruby>細<rt>ほそ</rt></ruby>なプライバシーを<ruby>明<rt>あか</rt></ruby>かすのが<ruby>最<rt>もっと</rt></ruby>も<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby><ruby>的<rt>てき</rt></ruby>である",
      "<ruby>人間関係<rt>にんげんかんけい</rt></ruby>の<ruby>深<rt>ふか</rt></ruby>さに<ruby>応<rt>おう</rt></ruby>じて、<ruby>相手<rt>あいて</rt></ruby>が<ruby>関<rt>かん</rt></ruby><ruby>心<rt>こころ</rt></ruby>を<ruby>向<rt>む</rt></ruby>けた<ruby>内<rt>うち</rt></ruby><ruby>容<rt>よう</rt></ruby>や<ruby>程<rt>てい</rt></ruby><ruby>度<rt>ど</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせて<ruby>吟<rt>ぎん</rt></ruby><ruby>味<rt>あじ</rt></ruby>して<ruby>開<rt>ひら</rt></ruby><ruby>示<rt>し</rt></ruby>する",
      "<ruby>援助者<rt>えんじょしゃ</rt></ruby>は<ruby>自分<rt>じぶん</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>は<ruby>絶<rt>ぜつ</rt></ruby><ruby>対<rt>たい</rt></ruby>に<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>開<rt>ひら</rt></ruby><ruby>示<rt>し</rt></ruby>してはならない",
      "<ruby>相手<rt>あいて</rt></ruby>が<ruby>嫌<rt>いや</rt></ruby>がっていても<ruby>強制<rt>きょうせい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>自己開示<rt>じこかいじ</rt></ruby>を<ruby>聞<rt>き</rt></ruby>かせるべきである"
    ],
    "answer": 2,
    "exp": "<ruby>出<rt>で</rt></ruby><ruby>会<rt>かい</rt></ruby>って<ruby>間<rt>あいだ</rt></ruby>もない<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>で<ruby>過<rt>か</rt></ruby><ruby>度<rt>ど</rt></ruby>なプライバシーを<ruby>明<rt>あか</rt></ruby>かすと<ruby>相手<rt>あいて</rt></ruby>に<ruby>違<rt>ちが</rt></ruby><ruby>和<rt>わ</rt></ruby><ruby>感<rt>かん</rt></ruby>を<ruby>与<rt>あた</rt></ruby>えるため、<ruby>関係<rt>かんけい</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>深<rt>ふか</rt></ruby>さに<ruby>応<rt>おう</rt></ruby>じた<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>開<rt>ひら</rt></ruby><ruby>示<rt>し</rt></ruby>が<ruby>求<rt>もと</rt></ruby>められます。"
  },
  {
    "id": 35,
    "stem": "<ruby>相<rt>そう</rt></ruby><ruby>互<rt>たが</rt></ruby>の<ruby>理解<rt>りかい</rt></ruby>と<ruby>信頼<rt>しんらい</rt></ruby>に<ruby>基<rt>き</rt></ruby>づき、<ruby>心<rt>こころ</rt></ruby>が<ruby>通<rt>つう</rt></ruby>い<ruby>合<rt>あ</rt></ruby>って<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>の<ruby>交<rt>こう</rt></ruby><ruby>流<rt>なが</rt></ruby>が<ruby>行<rt>こう</rt></ruby>われている<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>の<ruby>基<rt>き</rt></ruby><ruby>礎<rt>そ</rt></ruby>を<ruby>指<rt>ゆび</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>アドボカシー<rt>あどぼかしー</rt></ruby>",
      "<ruby>ラポール<rt>らぽーる</rt></ruby>",
      "アセスメント",
      "コーピング"
    ],
    "answer": 2,
    "exp": "<ruby>ラポール<rt>らぽーる</rt></ruby>（rapport）とは、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>と<ruby>援助者<rt>えんじょしゃ</rt></ruby>の<ruby>間<rt>あいだ</rt></ruby>に<ruby>心<rt>こころ</rt></ruby>が<ruby>通<rt>つう</rt></ruby>い<ruby>合<rt>あ</rt></ruby>い、<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>の<ruby>交<rt>こう</rt></ruby><ruby>流<rt>なが</rt></ruby>が<ruby>行<rt>こう</rt></ruby>われている<ruby>信頼<rt>しんらい</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>の<ruby>状態<rt>じょうたい</rt></ruby>をいいます。"
  },
  {
    "id": 36,
    "stem": "<ruby>人間関係<rt>にんげんかんけい</rt></ruby>における<ruby>ラポール<rt>らぽーる</rt></ruby>の<ruby>位置づけ<rt>いちづけ</rt></ruby>について<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>契<rt>けい</rt></ruby><ruby>約<rt>やく</rt></ruby>を<ruby>結<rt>けつ</rt></ruby>んだ<ruby>瞬<rt>しゅん</rt></ruby><ruby>間<rt>あいだ</rt></ruby>に<ruby>形<rt>かたち</rt></ruby><ruby>式<rt>しき</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>完<rt>かん</rt></ruby><ruby>成<rt>せい</rt></ruby>するものである",
      "<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>の<ruby>基<rt>き</rt></ruby><ruby>礎<rt>そ</rt></ruby>であり、<ruby>形成<rt>けいせい</rt></ruby>された<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>継続<rt>けいぞく</rt></ruby>・<ruby>発<rt>はつ</rt></ruby><ruby>展<rt>てん</rt></ruby>させていくことが<ruby>重要<rt>じゅうよう</rt></ruby>である",
      "<ruby>介護<rt>かいご</rt></ruby><ruby>技<rt>ぎ</rt></ruby><ruby>術<rt>じゅつ</rt></ruby>の<ruby>向<rt>む</rt></ruby><ruby>上<rt>うえ</rt></ruby>には<ruby>何<rt>なに</rt></ruby>の<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>も<ruby>与<rt>あた</rt></ruby>えない<ruby>二<rt>に</rt></ruby><ruby>次<rt>つぎ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>要素<rt>ようそ</rt></ruby>である",
      "<ruby>一<rt>いち</rt></ruby><ruby>度<rt>ど</rt></ruby><ruby>形成<rt>けいせい</rt></ruby>されれば<ruby>絶<rt>ぜつ</rt></ruby><ruby>対<rt>たい</rt></ruby>に<ruby>壊<rt>こわ</rt></ruby>れることのない<ruby>恒<rt>こう</rt></ruby><ruby>久<rt>ひさ</rt></ruby><ruby>的<rt>てき</rt></ruby>なものである"
    ],
    "answer": 2,
    "exp": "<ruby>ラポール<rt>らぽーる</rt></ruby>は<ruby>対<rt>たい</rt></ruby><ruby>人<rt>ひと</rt></ruby><ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>の<ruby>土<rt>つち</rt></ruby><ruby>台<rt>だい</rt></ruby>であり、<ruby>日<rt>ひ</rt></ruby>々の<ruby>誠実<rt>せいじつ</rt></ruby>な<ruby>関<rt>かん</rt></ruby>わりを<ruby>通<rt>つう</rt></ruby>じて<ruby>継続<rt>けいぞく</rt></ruby>・<ruby>維持<rt>いじ</rt></ruby>していく<ruby>努<rt>ど</rt></ruby><ruby>力<rt>ちから</rt></ruby>が<ruby>不可欠<rt>ふかけつ</rt></ruby>です。"
  },
  {
    "id": 37,
    "stem": "<ruby>人間関係<rt>にんげんかんけい</rt></ruby>を<ruby>形成<rt>けいせい</rt></ruby>する<ruby>上<rt>うえ</rt></ruby>で「<ruby>自分<rt>じぶん</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>可能性<rt>かのうせい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じる」ことの<ruby>具体例<rt>ぐたいれい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>第一印象<rt>だいいちいんしょう</rt></ruby>で<ruby>苦<rt>く</rt></ruby><ruby>手<rt>て</rt></ruby>と<ruby>感<rt>かん</rt></ruby>じた<ruby>相手<rt>あいて</rt></ruby>でも、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>の<ruby>枠組み<rt>わくぐみ</rt></ruby>を<ruby>見<rt>み</rt></ruby><ruby>直<rt>ちょく</rt></ruby>すことで<ruby>関係<rt>かんけい</rt></ruby>を<ruby>発<rt>はつ</rt></ruby><ruby>展<rt>てん</rt></ruby>させられると<ruby>考<rt>かんが</rt></ruby>える",
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby>は<ruby>一<rt>いち</rt></ruby><ruby>生<rt>せい</rt></ruby><ruby>絶<rt>ぜつ</rt></ruby><ruby>対<rt>たい</rt></ruby>に<ruby>変<rt>へん</rt></ruby>わらないと<ruby>信<rt>しん</rt></ruby>じて<ruby>自己主張<rt>じこしゅちょう</rt></ruby>を<ruby>曲<rt>きょく</rt></ruby>げない",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>に<ruby>無<rt>む</rt></ruby><ruby>条<rt>じょう</rt></ruby><ruby>件<rt>けん</rt></ruby>で<ruby>同<rt>おな</rt></ruby><ruby>調<rt>ちょう</rt></ruby>し、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>志<rt>し</rt></ruby>を<ruby>消<rt>き</rt></ruby><ruby>去<rt>きょ</rt></ruby>する",
      "<ruby>一<rt>いち</rt></ruby><ruby>度<rt>ど</rt></ruby><ruby>下<rt>した</rt></ruby>した<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>評価<rt>ひょうか</rt></ruby>は<ruby>二<rt>に</rt></ruby><ruby>度<rt>ど</rt></ruby>と<ruby>変<rt>へん</rt></ruby><ruby>更<rt>こう</rt></ruby>しない"
    ],
    "answer": 1,
    "exp": "<ruby>第一印象<rt>だいいちいんしょう</rt></ruby>での<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>は<ruby>自分<rt>じぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>み</rt></ruby>の<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>が<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>しており、<ruby>自<rt>じ</rt></ruby>らの<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>が<ruby>肯定的な方向<rt>こうていてきなほうこう</rt></ruby>へ<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>する<ruby>可能性<rt>かのうせい</rt></ruby>を<ruby>自覚<rt>じかく</rt></ruby>することが<ruby>大切<rt>たいせつ</rt></ruby>です。"
  },
  {
    "id": 38,
    "stem": "<ruby>相手<rt>あいて</rt></ruby>が<ruby>拒否的<rt>きょひてき</rt></ruby>な<ruby>態度<rt>たいど</rt></ruby>をとっているときの「<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>可能性<rt>かのうせい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じる」<ruby>姿勢<rt>しせい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "「<ruby>取<rt>と</rt></ruby>りつく<ruby>島<rt>しま</rt></ruby>もない」と<ruby>諦<rt>あきら</rt></ruby>めて<ruby>即<rt>そく</rt></ruby><ruby>座<rt>ざ</rt></ruby>に<ruby>関<rt>かん</rt></ruby>わりを<ruby>断<rt>だん</rt></ruby>ち<ruby>切<rt>き</rt></ruby>る",
      "<ruby>相手<rt>あいて</rt></ruby>が<ruby>変<rt>へん</rt></ruby>わる<ruby>可能性<rt>かのうせい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じ、<ruby>辛抱強く<rt>しんぼうづよく</rt></ruby><ruby>待<rt>ま</rt></ruby>ったり、<ruby>関<rt>かん</rt></ruby>わり<ruby>方<rt>かた</rt></ruby>を<ruby>工夫<rt>くふう</rt></ruby>したりする",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>を<ruby>叱責<rt>しっせき</rt></ruby>して<ruby>強<rt>つよ</rt></ruby><ruby>引<rt>ひ</rt></ruby>に<ruby>態度<rt>たいど</rt></ruby>を<ruby>改<rt>かい</rt></ruby>めさせる",
      "<ruby>家族<rt>かぞく</rt></ruby>に<ruby>連<rt>れん</rt></ruby><ruby>絡<rt>らく</rt></ruby>して<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>態度<rt>たいど</rt></ruby>を<ruby>非<rt>ひ</rt></ruby><ruby>難<rt>むずか</rt></ruby>する"
    ],
    "answer": 2,
    "exp": "<ruby>相手<rt>あいて</rt></ruby>が<ruby>拒否的<rt>きょひてき</rt></ruby>であっても、<ruby>将<rt>しょう</rt></ruby><ruby>来<rt>く</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>態度<rt>たいど</rt></ruby>が<ruby>軟<rt>なん</rt></ruby><ruby>化<rt>か</rt></ruby>・<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>する<ruby>可能性<rt>かのうせい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じ、<ruby>関<rt>かん</rt></ruby>わり<ruby>方<rt>かた</rt></ruby>を<ruby>工夫<rt>くふう</rt></ruby>しながら<ruby>辛抱強く<rt>しんぼうづよく</rt></ruby><ruby>待<rt>ま</rt></ruby>つ<ruby>姿勢<rt>しせい</rt></ruby>が<ruby>信頼<rt>しんらい</rt></ruby>を<ruby>生<rt>せい</rt></ruby>みます。"
  },
  {
    "id": 39,
    "stem": "<ruby>人間関係<rt>にんげんかんけい</rt></ruby>において「<ruby>社会の変化<rt>しゃかいのへんか</rt></ruby>に<ruby>敏感<rt>びんかん</rt></ruby>になる」ことの<ruby>重要<rt>じゅうよう</rt></ruby><ruby>性<rt>せい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>価値観<rt>かちかん</rt></ruby>や<ruby>制<rt>せい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>することで、<ruby>多<rt>おお</rt></ruby><ruby>様<rt>さま</rt></ruby>な<ruby>背<rt>せ</rt></ruby><ruby>景<rt>けい</rt></ruby>をもつ<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>生<rt>せい</rt></ruby>き<ruby>方<rt>かた</rt></ruby>を<ruby>柔軟<rt>じゅうなん</rt></ruby>に<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めることができる",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>流<rt>なが</rt></ruby><ruby>行<rt>こう</rt></ruby>にただ<ruby>流<rt>なが</rt></ruby>されて、<ruby>伝統的<rt>でんとうてき</rt></ruby>な<ruby>倫理<rt>りんり</rt></ruby>をすべて<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>するため",
      "<ruby>多数派<rt>たすうは</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>に<ruby>常<rt>じょう</rt></ruby>に<ruby>従<rt>したが</rt></ruby>い、<ruby>少数派<rt>しょうすうは</rt></ruby>を<ruby>排除<rt>はいじょ</rt></ruby>する<ruby>方<rt>かた</rt></ruby><ruby>針<rt>はり</rt></ruby>を<ruby>徹<rt>てつ</rt></ruby><ruby>底<rt>そこ</rt></ruby>するため",
      "<ruby>介護<rt>かいご</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>場<rt>ば</rt></ruby>の<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>最<rt>もっと</rt></ruby><ruby>新<rt>あたら</rt></ruby>のIT<ruby>技<rt>ぎ</rt></ruby><ruby>術<rt>じゅつ</rt></ruby>の<ruby>購<rt>こう</rt></ruby><ruby>入<rt>はい</rt></ruby>を<ruby>義<rt>ぎ</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>付<rt>つ</rt></ruby>けるため"
    ],
    "answer": 1,
    "exp": "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>価値観<rt>かちかん</rt></ruby>や<ruby>制<rt>せい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>（<ruby>多<rt>おお</rt></ruby><ruby>様<rt>さま</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>尊重<rt>そんちょう</rt></ruby>など）を<ruby>敏感<rt>びんかん</rt></ruby>に<ruby>捉<rt>とら</rt></ruby>えることは、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>生<rt>せい</rt></ruby>き<ruby>方<rt>かた</rt></ruby>や<ruby>尊厳<rt>そんげん</rt></ruby>への<ruby>理解<rt>りかい</rt></ruby>を<ruby>深<rt>ふか</rt></ruby>めるために<ruby>重要<rt>じゅうよう</rt></ruby>です。"
  },
  {
    "id": 40,
    "stem": "<ruby>性的マイノリティ<rt>せいてきまいのりてぃ</rt></ruby>（LGBTなど）や<ruby>多<rt>おお</rt></ruby><ruby>様<rt>さま</rt></ruby>な<ruby>生<rt>せい</rt></ruby>き<ruby>方<rt>かた</rt></ruby>への<ruby>理解<rt>りかい</rt></ruby>について<ruby>述<rt>じゅつ</rt></ruby>べた<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "「これまでの<ruby>自分<rt>じぶん</rt></ruby>の<ruby>常識<rt>じょうしき</rt></ruby>」にとらわれず、<ruby>相手<rt>あいて</rt></ruby>の<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>や<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby>に<ruby>共感<rt>きょうかん</rt></ruby>をもって<ruby>柔軟<rt>じゅうなん</rt></ruby>に<ruby>関<rt>かん</rt></ruby>わる",
      "<ruby>多数派<rt>たすうは</rt></ruby>の<ruby>生活様式<rt>せいかつようしき</rt></ruby>こそが<ruby>正<rt>せい</rt></ruby><ruby>常<rt>じょう</rt></ruby>であると<ruby>教<rt>おし</rt></ruby>え<ruby>諭<rt>ゆ</rt></ruby>す",
      "<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>性<rt>せい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>指<rt>ゆび</rt></ruby><ruby>向<rt>む</rt></ruby>は<ruby>介護<rt>かいご</rt></ruby>や<ruby>福<rt>ふく</rt></ruby><ruby>祉<rt>し</rt></ruby>の<ruby>現<rt>げん</rt></ruby><ruby>場<rt>ば</rt></ruby>では<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>考<rt>かんが</rt></ruby><ruby>慮<rt>りょ</rt></ruby>する<ruby>必要<rt>ひつよう</rt></ruby>がない",
      "<ruby>少数派<rt>しょうすうは</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>は<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>調<rt>ちょう</rt></ruby><ruby>和<rt>わ</rt></ruby>を<ruby>乱<rt>らん</rt></ruby>すため<ruby>公<rt>こう</rt></ruby>の<ruby>場<rt>ば</rt></ruby>では<ruby>無<rt>む</rt></ruby><ruby>視<rt>し</rt></ruby>すべきである"
    ],
    "answer": 1,
    "exp": "<ruby>多<rt>おお</rt></ruby><ruby>様<rt>さま</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>々を<ruby>理解<rt>りかい</rt></ruby>するには、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>固定観念<rt>こていかんねん</rt></ruby>や<ruby>常識<rt>じょうしき</rt></ruby>を<ruby>疑<rt>ぎ</rt></ruby>い、その<ruby>人<rt>ひと</rt></ruby>の<ruby>立ち位置<rt>たちいち</rt></ruby>から<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>や<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby>を<ruby>共感<rt>きょうかん</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>捉<rt>とら</rt></ruby>える<ruby>姿勢<rt>しせい</rt></ruby>が<ruby>不可欠<rt>ふかけつ</rt></ruby>です。"
  },
  {
    "id": 41,
    "stem": "「<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>」を<ruby>尊重<rt>そんちょう</rt></ruby>することに<ruby>含<rt>ふく</rt></ruby>まれる2つの<ruby>側面<rt>そくめん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "「<ruby>人間<rt>にんげん</rt></ruby>としての<ruby>尊厳<rt>そんげん</rt></ruby>（<ruby>人間<rt>にんげん</rt></ruby>らしさ）」と「<ruby>個<rt>こ</rt></ruby>々<ruby>人<rt>ひと</rt></ruby>の<ruby>具<rt>ぐ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>暮<rt>く</rt></ruby>らしや<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby>における<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>」",
      "「<ruby>身<rt>み</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby>の<ruby>高<rt>たか</rt></ruby>さ」と「<ruby>経<rt>けい</rt></ruby><ruby>済<rt>さい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>裕<rt>ゆう</rt></ruby><ruby>福<rt>ふく</rt></ruby>さ」",
      "「<ruby>家族<rt>かぞく</rt></ruby>と<ruby>同居<rt>どうきょ</rt></ruby>しているか」と「<ruby>施設<rt>しせつ</rt></ruby>に<ruby>入所<rt>にゅうしょ</rt></ruby>しているか」",
      "「<ruby>知能指数<rt>ちのうしすう</rt></ruby>の<ruby>高<rt>たか</rt></ruby>さ」と「<ruby>学歴<rt>がくれき</rt></ruby>の<ruby>高<rt>たか</rt></ruby>さ」"
    ],
    "answer": 1,
    "exp": "<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>の<ruby>尊重<rt>そんちょう</rt></ruby>には、<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby>の<ruby>人<rt>ひと</rt></ruby><ruby>権<rt>けん</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>障<rt>しょう</rt></ruby>に<ruby>基<rt>き</rt></ruby>づく「<ruby>人間<rt>にんげん</rt></ruby>としての<ruby>尊厳<rt>そんげん</rt></ruby>」と、<ruby>固<rt>かた</rt></ruby><ruby>有<rt>ゆう</rt></ruby>の<ruby>生活歴<rt>せいかつれき</rt></ruby>に<ruby>基<rt>き</rt></ruby>づく「<ruby>具<rt>ぐ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>個<rt>こ</rt></ruby><ruby>性<rt>せい</rt></ruby>」の<ruby>両<rt>りょう</rt></ruby><ruby>面<rt>めん</rt></ruby>があります。"
  },
  {
    "id": 42,
    "stem": "<ruby>対人援助職<rt>たいじんえんじょしょく</rt></ruby>が<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の「<ruby>その人らしさ<rt>そのひとらしさ</rt></ruby>」を<ruby>支<rt>し</rt></ruby>えるために<ruby>果<rt>か</rt></ruby>たすべき<ruby>役割<rt>やくわり</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>生活歴<rt>せいかつれき</rt></ruby>や<ruby>大切<rt>たいせつ</rt></ruby>にしてきた<ruby>価値観<rt>かちかん</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>し、その<ruby>人<rt>ひと</rt></ruby>らしく<ruby>生<rt>せい</rt></ruby>きられるよう<ruby>支援<rt>しえん</rt></ruby>する",
      "<ruby>施設<rt>しせつ</rt></ruby><ruby>側<rt>がわ</rt></ruby>の<ruby>効<rt>こう</rt></ruby><ruby>率<rt>りつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>スケジュール<rt>すけじゅーる</rt></ruby>に<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>生活リズム<rt>せいかつりずむ</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>従<rt>したが</rt></ruby>わせる",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>過<rt>か</rt></ruby><ruby>去<rt>きょ</rt></ruby>に<ruby>培<rt>ばい</rt></ruby>ってきた<ruby>習<rt>しゅう</rt></ruby><ruby>慣<rt>な</rt></ruby>をすべて<ruby>捨<rt>す</rt></ruby>てさせ、<ruby>新<rt>あたら</rt></ruby>しいルールを<ruby>強制<rt>きょうせい</rt></ruby>する",
      "すべての<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>画一的<rt>かくいつてき</rt></ruby>で<ruby>同<rt>おな</rt></ruby><ruby>一<rt>いち</rt></ruby>の<ruby>ケアプラン<rt>けあぷらん</rt></ruby>を<ruby>適<rt>てき</rt></ruby><ruby>用<rt>よう</rt></ruby>する"
    ],
    "answer": 1,
    "exp": "その<ruby>人<rt>ひと</rt></ruby>の<ruby>歩<rt>ほ</rt></ruby>んできた<ruby>歴<rt>れき</rt></ruby><ruby>史<rt>し</rt></ruby>や<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby><ruby>観<rt>かん</rt></ruby>に<ruby>寄り添い<rt>よりそい</rt></ruby>、<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>と<ruby>主体<rt>しゅたい</rt></ruby><ruby>性<rt>せい</rt></ruby>が<ruby>保<rt>ほ</rt></ruby>たれるように<ruby>支援<rt>しえん</rt></ruby>することが<ruby>介護福祉職<rt>かいごふくししょく</rt></ruby>の<ruby>本<rt>ほん</rt></ruby><ruby>質<rt>しつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>役割<rt>やくわり</rt></ruby>です。"
  },
  {
    "id": 43,
    "stem": "<ruby>対<rt>たい</rt></ruby><ruby>人<rt>ひと</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>における「<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby><ruby>性<rt>せい</rt></ruby>と<ruby>違<rt>ちが</rt></ruby>い」の<ruby>捉<rt>とら</rt></ruby>え<ruby>方<rt>かた</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>親<rt>おや</rt></ruby>しい<ruby>間<rt>あいだ</rt></ruby><ruby>柄<rt>がら</rt></ruby>であっても<ruby>他者<rt>たしゃ</rt></ruby>は<ruby>自分<rt>じぶん</rt></ruby>とは<ruby>異<rt>い</rt></ruby>なる<ruby>人格<rt>じんかく</rt></ruby>であり、<ruby>同一視<rt>どういつし</rt></ruby>してはならない",
      "<ruby>仲<rt>なか</rt></ruby>が<ruby>良<rt>よ</rt></ruby>い<ruby>関係<rt>かんけい</rt></ruby>であれば、<ruby>相手<rt>あいて</rt></ruby>も<ruby>自分<rt>じぶん</rt></ruby>とまったく<ruby>同<rt>おな</rt></ruby>じ<ruby>考<rt>かんが</rt></ruby>えを<ruby>持<rt>も</rt></ruby>っているとみなしてよい",
      "<ruby>違<rt>ちが</rt></ruby>いを<ruby>見<rt>み</rt></ruby>つけたら、どちらが<ruby>正<rt>せい</rt></ruby>しいかを<ruby>議<rt>ぎ</rt></ruby><ruby>論<rt>ろん</rt></ruby>して<ruby>白<rt>しろ</rt></ruby><ruby>黒<rt>くろ</rt></ruby>つけるべきである",
      "<ruby>共通点<rt>きょうつうてん</rt></ruby>がない<ruby>相手<rt>あいて</rt></ruby>とは<ruby>良<rt>よ</rt></ruby><ruby>好<rt>す</rt></ruby>な<ruby>関係<rt>かんけい</rt></ruby>を<ruby>築<rt>ちく</rt></ruby>くことは<ruby>不<rt>ふ</rt></ruby><ruby>可<rt>か</rt></ruby><ruby>能<rt>のう</rt></ruby>である"
    ],
    "answer": 1,
    "exp": "<ruby>親<rt>おや</rt></ruby>しい<ruby>関係<rt>かんけい</rt></ruby>であっても<ruby>他者<rt>たしゃ</rt></ruby>を<ruby>自分<rt>じぶん</rt></ruby>と<ruby>同一視<rt>どういつし</rt></ruby>せず、<ruby>別<rt>べつ</rt></ruby><ruby>個<rt>こ</rt></ruby>の<ruby>人格<rt>じんかく</rt></ruby>として<ruby>違<rt>ちが</rt></ruby>いを<ruby>尊重<rt>そんちょう</rt></ruby>することが<ruby>健全<rt>けんぜん</rt></ruby>な<ruby>人間関係<rt>にんげんかんけい</rt></ruby>の<ruby>前<rt>まえ</rt></ruby><ruby>提<rt>てい</rt></ruby>です。"
  },
  {
    "id": 44,
    "stem": "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>自分<rt>じぶん</rt></ruby>の<ruby>内面<rt>ないめん</rt></ruby>を<ruby>表現<rt>ひょうげん</rt></ruby>する<ruby>際<rt>さい</rt></ruby>の<ruby>特徴<rt>とくちょう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>思<rt>おも</rt></ruby>いは、<ruby>必<rt>ひつ</rt></ruby>ずしも<ruby>言葉<rt>ことば</rt></ruby>や<ruby>目<rt>め</rt></ruby>に<ruby>見<rt>み</rt></ruby>える<ruby>形<rt>かたち</rt></ruby>だけで<ruby>表現<rt>ひょうげん</rt></ruby>されるとは<ruby>限<rt>げん</rt></ruby>らない",
      "<ruby>本<rt>ほん</rt></ruby><ruby>音<rt>おと</rt></ruby>は<ruby>必<rt>ひつ</rt></ruby>ず<ruby>最<rt>もっと</rt></ruby><ruby>初<rt>しょ</rt></ruby>の<ruby>大<rt>おお</rt></ruby><ruby>声<rt>こえ</rt></ruby>での<ruby>発<rt>はつ</rt></ruby><ruby>言<rt>げん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>にすべて<ruby>含<rt>ふく</rt></ruby>まれている",
      "<ruby>表情<rt>ひょうじょう</rt></ruby>と<ruby>内面<rt>ないめん</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>は<ruby>常<rt>じょう</rt></ruby>に<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>一<rt>いち</rt></ruby><ruby>致<rt>ち</rt></ruby>しているため<ruby>深<rt>ふか</rt></ruby><ruby>読<rt>よ</rt></ruby>みは<ruby>不<rt>ふ</rt></ruby><ruby>要<rt>よう</rt></ruby>である",
      "<ruby>言葉<rt>ことば</rt></ruby>が<ruby>出<rt>で</rt></ruby>ない<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>心<rt>こころ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていない"
    ],
    "answer": 1,
    "exp": "<ruby>人<rt>ひと</rt></ruby>は<ruby>内面<rt>ないめん</rt></ruby>の<ruby>複<rt>ふく</rt></ruby><ruby>雑<rt>ざつ</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>目<rt>め</rt></ruby>に<ruby>見<rt>み</rt></ruby>える<ruby>形<rt>かたち</rt></ruby>で<ruby>表現<rt>ひょうげん</rt></ruby>するとは<ruby>限<rt>げん</rt></ruby>らず、<ruby>非<rt>ひ</rt></ruby><ruby>言語<rt>げんご</rt></ruby><ruby>的<rt>てき</rt></ruby>なサインや<ruby>沈黙<rt>ちんもく</rt></ruby>の<ruby>中<rt>なか</rt></ruby>にも<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>思<rt>おも</rt></ruby>いが<ruby>込<rt>こ</rt></ruby>められています。"
  },
  {
    "id": 45,
    "stem": "<ruby>他者<rt>たしゃ</rt></ruby><ruby>理解<rt>りかい</rt></ruby>において「<ruby>自分流<rt>じぶんりゅう</rt></ruby>の<ruby>他者<rt>たしゃ</rt></ruby><ruby>理解<rt>りかい</rt></ruby>」にとどまることの<ruby>危険性<rt>きけんせい</rt></ruby>を<ruby>回避<rt>かいひ</rt></ruby>する<ruby>態度<rt>たいど</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>解<rt>かい</rt></ruby><ruby>釈<rt>しゃく</rt></ruby>が<ruby>絶<rt>ぜつ</rt></ruby><ruby>対<rt>たい</rt></ruby>であると<ruby>思<rt>おも</rt></ruby>い<ruby>込<rt>こ</rt></ruby>まず、<ruby>常<rt>じょう</rt></ruby>に<ruby>相手<rt>あいて</rt></ruby>の<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>を<ruby>確<rt>かく</rt></ruby>かめながら<ruby>理解<rt>りかい</rt></ruby>を<ruby>修<rt>しゅう</rt></ruby><ruby>正<rt>せい</rt></ruby>していく",
      "<ruby>最<rt>もっと</rt></ruby><ruby>初<rt>しょ</rt></ruby>に<ruby>立<rt>た</rt></ruby>てた<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby><ruby>物<rt>もの</rt></ruby><ruby>像<rt>ぞう</rt></ruby>を<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>変<rt>へん</rt></ruby>えずに<ruby>対<rt>たい</rt></ruby><ruby>応<rt>おう</rt></ruby>を<ruby>固定化<rt>こていか</rt></ruby>する",
      "<ruby>同僚<rt>どうりょう</rt></ruby>や<ruby>他<rt>た</rt></ruby><ruby>職<rt>しょく</rt></ruby><ruby>種<rt>しゅ</rt></ruby>からの<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>観察記録<rt>かんさつきろく</rt></ruby>は<ruby>見<rt>み</rt></ruby>ずに<ruby>自分<rt>じぶん</rt></ruby>の<ruby>直感<rt>ちょっかん</rt></ruby>だけを<ruby>信<rt>しん</rt></ruby>じる",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>言<rt>げん</rt></ruby>をすべて<ruby>文字<rt>もじ</rt></ruby><ruby>通<rt>つう</rt></ruby>りの<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>だけで<ruby>機械<rt>きかい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>処<rt>しょ</rt></ruby><ruby>理<rt>り</rt></ruby>する"
    ],
    "answer": 1,
    "exp": "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>見<rt>み</rt></ruby><ruby>方<rt>かた</rt></ruby>はあくまで「<ruby>自分流<rt>じぶんりゅう</rt></ruby>」であると<ruby>謙<rt>けん</rt></ruby><ruby>虚<rt>きょ</rt></ruby>に<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>め、<ruby>相手<rt>あいて</rt></ruby>の<ruby>言動<rt>げんどう</rt></ruby>や<ruby>多職種<rt>たしょくしゅ</rt></ruby>の<ruby>視点<rt>してん</rt></ruby>を<ruby>交<rt>こう</rt></ruby>えて<ruby>修<rt>しゅう</rt></ruby><ruby>正<rt>せい</rt></ruby>し<ruby>続<rt>ぞく</rt></ruby>ける<ruby>姿勢<rt>しせい</rt></ruby>が<ruby>大切<rt>たいせつ</rt></ruby>です。"
  },
  {
    "id": 46,
    "stem": "<ruby>介護福祉士<rt>かいごふくしし</rt></ruby>が「<ruby>人間<rt>にんげん</rt></ruby><ruby>理解<rt>りかい</rt></ruby>」を<ruby>深<rt>ふか</rt></ruby>める<ruby>究極の目的<rt>きゅうきょくのもくてき</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>を<ruby>保持<rt>ほじ</rt></ruby>し、<ruby>自立<rt>じりつ</rt></ruby>を<ruby>支援<rt>しえん</rt></ruby>するために<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>信頼<rt>しんらい</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>を<ruby>形成<rt>けいせい</rt></ruby>するため",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>弱点<rt>じゃくてん</rt></ruby>を<ruby>把<rt>は</rt></ruby><ruby>握<rt>にぎ</rt></ruby>して<ruby>施設<rt>しせつ</rt></ruby><ruby>側<rt>がわ</rt></ruby>の<ruby>管<rt>かん</rt></ruby><ruby>理<rt>り</rt></ruby>を<ruby>容<rt>よう</rt></ruby><ruby>易<rt>い</rt></ruby>にするため",
      "<ruby>介護<rt>かいご</rt></ruby><ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>の<ruby>所要時間<rt>しょようじかん</rt></ruby>を<ruby>短縮<rt>たんしゅく</rt></ruby>して<ruby>人<rt>ひと</rt></ruby><ruby>件<rt>けん</rt></ruby><ruby>費<rt>ひ</rt></ruby>を<ruby>削減<rt>さくげん</rt></ruby>するため",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>個人的<rt>こじんてき</rt></ruby>な<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby>を<ruby>収<rt>しゅう</rt></ruby><ruby>集<rt>しゅう</rt></ruby>して<ruby>他<rt>た</rt></ruby><ruby>職<rt>しょく</rt></ruby><ruby>種<rt>しゅ</rt></ruby>との<ruby>雑<rt>ざつ</rt></ruby><ruby>談<rt>だん</rt></ruby>に<ruby>活<rt>かつ</rt></ruby><ruby>用<rt>よう</rt></ruby>するため"
    ],
    "answer": 1,
    "exp": "<ruby>人間<rt>にんげん</rt></ruby><ruby>理解<rt>りかい</rt></ruby>を<ruby>深<rt>ふか</rt></ruby>めることは、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>を<ruby>守<rt>まも</rt></ruby>り、<ruby>一<rt>いち</rt></ruby><ruby>人<rt>ひと</rt></ruby>ひとりの<ruby>自立支援<rt>じりつしえん</rt></ruby>に<ruby>向<rt>む</rt></ruby>けた<ruby>信頼<rt>しんらい</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>を<ruby>築<rt>ちく</rt></ruby>くための<ruby>大<rt>おお</rt></ruby><ruby>前<rt>まえ</rt></ruby><ruby>提<rt>てい</rt></ruby>となります。"
  },
  {
    "id": 47,
    "stem": "<ruby>日本国憲法第<rt>にほんこくけんぽうだい</rt></ruby>13<ruby>条前段<rt>じょうぜんだん</rt></ruby>で<ruby>規<rt>き</rt></ruby><ruby>定<rt>てい</rt></ruby>されている「<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>」に<ruby>関<rt>かん</rt></ruby>する<ruby>文言<rt>もんごん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>労<rt>ろう</rt></ruby><ruby>働<rt>はたら</rt></ruby><ruby>者<rt>しゃ</rt></ruby>として<ruby>評価<rt>ひょうか</rt></ruby>される",
      "すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>として<ruby>尊重<rt>そんちょう</rt></ruby>される",
      "すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>国<rt>くに</rt></ruby><ruby>家<rt>いえ</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>展<rt>てん</rt></ruby>のために<ruby>奉<rt>ほう</rt></ruby><ruby>仕<rt>し</rt></ruby>する",
      "すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>家族<rt>かぞく</rt></ruby>の<ruby>代<rt>だい</rt></ruby><ruby>表<rt>ひょう</rt></ruby>として<ruby>遇<rt>ぐう</rt></ruby>される"
    ],
    "answer": 2,
    "exp": "<ruby>日本国憲法第<rt>にほんこくけんぽうだい</rt></ruby>13<ruby>条前段<rt>じょうぜんだん</rt></ruby>には「すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>として<ruby>尊重<rt>そんちょう</rt></ruby>される」と<ruby>明<rt>あか</rt></ruby><ruby>記<rt>き</rt></ruby>されており、<ruby>人<rt>ひと</rt></ruby><ruby>権<rt>けん</rt></ruby>の<ruby>基本<rt>きほん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>念<rt>ねん</rt></ruby>となっています。"
  },
  {
    "id": 48,
    "stem": "<ruby>日本国憲法第<rt>にほんこくけんぽうだい</rt></ruby>25<ruby>条<rt>じょう</rt></ruby><ruby>第<rt>だい</rt></ruby>1<ruby>項<rt>こう</rt></ruby>が<ruby>保<rt>ほ</rt></ruby><ruby>障<rt>しょう</rt></ruby>する「<ruby>生存権<rt>せいぞんけん</rt></ruby>」の<ruby>理<rt>り</rt></ruby><ruby>念<rt>ねん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>健康で文化的な最低限度の生活<rt>けんこうでぶんかてきなさいていげんどのせいかつ</rt></ruby>を<ruby>営<rt>えい</rt></ruby>む<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>",
      "いかなる<ruby>場<rt>ば</rt></ruby><ruby>合<rt>あ</rt></ruby>も<ruby>労<rt>ろう</rt></ruby><ruby>働<rt>はたら</rt></ruby>を<ruby>免<rt>めん</rt></ruby><ruby>除<rt>じょ</rt></ruby>される<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>",
      "すべての<ruby>国民<rt>こくみん</rt></ruby>に<ruby>均<rt>きん</rt></ruby><ruby>一<rt>いち</rt></ruby>な<ruby>公的年金<rt>こうてきねんきん</rt></ruby>を<ruby>無<rt>む</rt></ruby><ruby>条<rt>じょう</rt></ruby><ruby>件<rt>けん</rt></ruby><ruby>支<rt>し</rt></ruby><ruby>給<rt>きゅう</rt></ruby>する<ruby>義<rt>ぎ</rt></ruby><ruby>務<rt>む</rt></ruby>",
      "<ruby>経<rt>けい</rt></ruby><ruby>済<rt>さい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>競<rt>きょう</rt></ruby><ruby>争<rt>そう</rt></ruby>に<ruby>勝<rt>か</rt></ruby><ruby>利<rt>り</rt></ruby>した<ruby>者<rt>しゃ</rt></ruby>のみが<ruby>生存<rt>せいぞん</rt></ruby>できる<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>憲<rt>けん</rt></ruby><ruby>法<rt>ほう</rt></ruby><ruby>第<rt>だい</rt></ruby>25<ruby>条<rt>じょう</rt></ruby><ruby>第<rt>だい</rt></ruby>1<ruby>項<rt>こう</rt></ruby>は「すべて<ruby>国民<rt>こくみん</rt></ruby>は、<ruby>健康で文化的な最低限度の生活<rt>けんこうでぶんかてきなさいていげんどのせいかつ</rt></ruby>を<ruby>営<rt>えい</rt></ruby>む<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>を<ruby>有<rt>ゆう</rt></ruby>する」と<ruby>定<rt>てい</rt></ruby>めています。"
  },
  {
    "id": 49,
    "stem": "1834<ruby>年<rt>ねん</rt></ruby>のイギリス<ruby>新救貧法<rt>しんきゅうひんほう</rt></ruby>において<ruby>採<rt>さい</rt></ruby><ruby>用<rt>よう</rt></ruby>された「<ruby>劣等処遇の原則<rt>れっとうしょぐうのげんそく</rt></ruby>」の<ruby>説<rt>せつ</rt></ruby><ruby>明<rt>あか</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>救済<rt>きゅうさい</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける<ruby>貧民<rt>ひんみん</rt></ruby>の<ruby>生活水準<rt>せいかつすいじゅん</rt></ruby>は、<ruby>最下級<rt>さいかきゅう</rt></ruby>の<ruby>独立労働者<rt>どくりつろうどうしゃ</rt></ruby>の<ruby>生活条件以下<rt>せいかつじょうけんいか</rt></ruby>でなければならない",
      "<ruby>障害<rt>しょうがい</rt></ruby>をもつ<ruby>人<rt>ひと</rt></ruby>々を<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>主流<rt>しゅりゅう</rt></ruby>の<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>条<rt>じょう</rt></ruby><ruby>件<rt>けん</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>づけること",
      "<ruby>救済<rt>きゅうさい</rt></ruby><ruby>対象<rt>たいしょう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>無<rt>む</rt></ruby><ruby>制<rt>せい</rt></ruby><ruby>限<rt>げん</rt></ruby>の<ruby>居<rt>きょ</rt></ruby><ruby>宅<rt>たく</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>護<rt>ご</rt></ruby>と<ruby>金銭給付<rt>きんせんきゅうふ</rt></ruby>を<ruby>行<rt>こう</rt></ruby>うこと",
      "<ruby>労<rt>ろう</rt></ruby><ruby>働<rt>はたら</rt></ruby><ruby>能力<rt>のうりょく</rt></ruby>のない<ruby>者<rt>しゃ</rt></ruby>にも<ruby>重労働<rt>じゅうろうどう</rt></ruby>を<ruby>課<rt>か</rt></ruby>して<ruby>処刑<rt>しょけい</rt></ruby>すること"
    ],
    "answer": 1,
    "exp": "<ruby>劣等処遇の原則<rt>れっとうしょぐうのげんそく</rt></ruby>とは、<ruby>公<rt>こう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>救済<rt>きゅうさい</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける<ruby>者<rt>しゃ</rt></ruby>の<ruby>生活水準<rt>せいかつすいじゅん</rt></ruby>を<ruby>自立<rt>じりつ</rt></ruby>して<ruby>働<rt>はたら</rt></ruby>く<ruby>最<rt>もっと</rt></ruby><ruby>下<rt>した</rt></ruby><ruby>層<rt>そう</rt></ruby>の<ruby>労<rt>ろう</rt></ruby><ruby>働<rt>はたら</rt></ruby><ruby>者<rt>しゃ</rt></ruby>より<ruby>低<rt>てい</rt></ruby>く<ruby>抑<rt>よく</rt></ruby>えるという<ruby>厳<rt>げん</rt></ruby>しい<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>です。"
  },
  {
    "id": 50,
    "stem": "<ruby>ノーマライゼーション<rt>のーまらいぜーしょん</rt></ruby>の<ruby>理<rt>り</rt></ruby><ruby>念<rt>ねん</rt></ruby>を<ruby>世<rt>せ</rt></ruby><ruby>界<rt>かい</rt></ruby>で<ruby>初<rt>しょ</rt></ruby>めて<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>し、デンマークの1959<ruby>年<rt>ねん</rt></ruby><ruby>法<rt>ほう</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>立<rt>た</rt></ruby>に<ruby>尽<rt>じん</rt></ruby><ruby>力<rt>ちから</rt></ruby>した「<ruby>生みの親<rt>うみのおや</rt></ruby>」として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "バンク＝ミケルセン",
      "ニィリエ",
      "ヴォルフェンスベルガー",
      "パウル・ナトルプ"
    ],
    "answer": 1,
    "exp": "バンク＝ミケルセンは、<ruby>知的障害者<rt>ちてきしょうがいしゃ</rt></ruby>の<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>条<rt>じょう</rt></ruby><ruby>件<rt>けん</rt></ruby>を<ruby>健<rt>けん</rt></ruby><ruby>常<rt>じょう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>生活リズム<rt>せいかつりずむ</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>づける<ruby>ノーマライゼーション<rt>のーまらいぜーしょん</rt></ruby>を<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>しました。"
  },
  {
    "id": 51,
    "stem": "スウェーデンのニィリエ（Nirje）が<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した「<ruby>ノーマライゼーション<rt>のーまらいぜーしょん</rt></ruby>の8つの<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>」に<ruby>含<rt>ふく</rt></ruby>まれないものを1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "1<ruby>日<rt>ひ</rt></ruby>のノーマルなリズム",
      "<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby>のノーマルな<ruby>経験<rt>けいけん</rt></ruby>（ライフサイクル）",
      "<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>な<ruby>隔離施設<rt>かくりしせつ</rt></ruby>での<ruby>生涯管理<rt>しょうがいかんり</rt></ruby>",
      "<ruby>男<rt>おとこ</rt></ruby><ruby>女<rt>おんな</rt></ruby><ruby>両<rt>りょう</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>世<rt>せ</rt></ruby><ruby>界<rt>かい</rt></ruby>での<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>"
    ],
    "answer": 3,
    "exp": "ニィリエの8つの<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>には「<ruby>隔離施設<rt>かくりしせつ</rt></ruby>での<ruby>管<rt>かん</rt></ruby><ruby>理<rt>り</rt></ruby>」は<ruby>含<rt>ふく</rt></ruby>まれず、<ruby>地域社会<rt>ちいきしゃかい</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>普<rt>ふ</rt></ruby><ruby>通<rt>つう</rt></ruby>の<ruby>生活リズム<rt>せいかつりずむ</rt></ruby>を<ruby>送<rt>おく</rt></ruby>ることが<ruby>強<rt>つよ</rt></ruby><ruby>調<rt>ちょう</rt></ruby>されています。"
  },
  {
    "id": 52,
    "stem": "<ruby>現代<rt>げんだい</rt></ruby>の<ruby>介護<rt>かいご</rt></ruby><ruby>福<rt>ふく</rt></ruby><ruby>祉<rt>し</rt></ruby>における「<ruby>自立<rt>じりつ</rt></ruby>」の<ruby>捉<rt>とら</rt></ruby>え<ruby>方<rt>かた</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>誰<rt>だれ</rt></ruby>の<ruby>助<rt>じょ</rt></ruby>けも<ruby>借<rt>か</rt></ruby>りずに、すべての<ruby>日常生活動作<rt>にちじょうせいかつどうさ</rt></ruby>を1<ruby>人<rt>ひと</rt></ruby>だけで<ruby>完<rt>かん</rt></ruby><ruby>結<rt>けつ</rt></ruby>すること",
      "<ruby>自己選択<rt>じこせんたく</rt></ruby>・<ruby>自己決定<rt>じこけってい</rt></ruby>に<ruby>基<rt>き</rt></ruby>づき、<ruby>必要<rt>ひつよう</rt></ruby>なときは<ruby>他者<rt>たしゃ</rt></ruby>に<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>依存<rt>いぞん</rt></ruby>をしながら<ruby>主体<rt>しゅたい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>暮<rt>く</rt></ruby>らすこと",
      "すべての<ruby>行<rt>こう</rt></ruby><ruby>動<rt>どう</rt></ruby>や<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>を<ruby>家族<rt>かぞく</rt></ruby>や<ruby>介護<rt>かいご</rt></ruby><ruby>職<rt>しょく</rt></ruby><ruby>員<rt>いん</rt></ruby>に<ruby>委<rt>い</rt></ruby>ねて<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>すること",
      "<ruby>身<rt>み</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>機能回復<rt>きのうかいふく</rt></ruby>のみを<ruby>目<rt>め</rt></ruby><ruby>標<rt>ひょう</rt></ruby>とし、<ruby>社会参加<rt>しゃかいさんか</rt></ruby>は<ruby>諦<rt>あきら</rt></ruby>めること"
    ],
    "answer": 2,
    "exp": "<ruby>自立<rt>じりつ</rt></ruby>とは<ruby>何<rt>なに</rt></ruby>でも1<ruby>人<rt>ひと</rt></ruby>で<ruby>抱<rt>だ</rt></ruby>え<ruby>込<rt>こ</rt></ruby>むことではなく、<ruby>自<rt>じ</rt></ruby>らの<ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby>で<ruby>選<rt>せん</rt></ruby><ruby>択<rt>たく</rt></ruby>・<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>し、<ruby>適<rt>てき</rt></ruby><ruby>度<rt>ど</rt></ruby>な<ruby>他者<rt>たしゃ</rt></ruby>への<ruby>依存<rt>いぞん</rt></ruby>や<ruby>助<rt>じょ</rt></ruby><ruby>力<rt>ちから</rt></ruby>を<ruby>活<rt>かつ</rt></ruby><ruby>用<rt>よう</rt></ruby>しながら<ruby>生<rt>せい</rt></ruby>きることです。"
  },
  {
    "id": 53,
    "stem": "<ruby>自立支援<rt>じりつしえん</rt></ruby>において、<ruby>病<rt>びょう</rt></ruby><ruby>気<rt>き</rt></ruby>やけがで<ruby>失<rt>しつ</rt></ruby>われた<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>外<rt>そと</rt></ruby>の「<ruby>残<rt>ざん</rt></ruby>された<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby>」を<ruby>活<rt>かつ</rt></ruby>かすことを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶか<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>廃用機能<rt>はいようきのう</rt></ruby>の<ruby>固<rt>かた</rt></ruby><ruby>定<rt>てい</rt></ruby>",
      "<ruby>残存機能<rt>ざんぞんきのう</rt></ruby>（<ruby>活用可能能力<rt>かつようかのうのうりょく</rt></ruby>）の<ruby>活<rt>かつ</rt></ruby><ruby>用<rt>よう</rt></ruby>",
      "<ruby>全面介護<rt>ぜんめんかいご</rt></ruby>の<ruby>適<rt>てき</rt></ruby><ruby>用<rt>よう</rt></ruby>",
      "<ruby>代償行為<rt>だいしょうこうい</rt></ruby>の<ruby>全<rt>ぜん</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>禁止<rt>きんし</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>自立支援<rt>じりつしえん</rt></ruby>では、<ruby>残<rt>ざん</rt></ruby>された「<ruby>残存機能<rt>ざんぞんきのう</rt></ruby>」を<ruby>見<rt>み</rt></ruby><ruby>極<rt>きょく</rt></ruby>め、それを<ruby>最<rt>もっと</rt></ruby><ruby>大<rt>おお</rt></ruby><ruby>限<rt>げん</rt></ruby>に<ruby>活<rt>かつ</rt></ruby>かして<ruby>自力<rt>じりき</rt></ruby>で<ruby>行<rt>こう</rt></ruby>える<ruby>喜<rt>よろこ</rt></ruby>びや<ruby>意<rt>い</rt></ruby><ruby>欲<rt>よく</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>で</rt></ruby>すことが<ruby>重要<rt>じゅうよう</rt></ruby>です。"
  },
  {
    "id": 54,
    "stem": "2001<ruby>年<rt>ねん</rt></ruby>にWHOが<ruby>採<rt>さい</rt></ruby><ruby>択<rt>たく</rt></ruby>した<ruby>国際生活機能分類<rt>こくさいせいかつきのうぶんるい</rt></ruby>（ICF）の<ruby>基本<rt>きほん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>特徴<rt>とくちょう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>病<rt>びょう</rt></ruby><ruby>気<rt>き</rt></ruby>や<ruby>障害<rt>しょうがい</rt></ruby>というマイナス<ruby>面<rt>めん</rt></ruby>だけでなく、「<ruby>生活機能<rt>せいかつきのう</rt></ruby>」というプラス<ruby>面<rt>めん</rt></ruby>に<ruby>着<rt>ちゃく</rt></ruby><ruby>目<rt>め</rt></ruby>して<ruby>双<rt>そう</rt></ruby><ruby>方<rt>かた</rt></ruby><ruby>向<rt>む</rt></ruby>の<ruby>相<rt>そう</rt></ruby><ruby>互<rt>たが</rt></ruby><ruby>作<rt>つく</rt></ruby><ruby>用<rt>よう</rt></ruby>として<ruby>捉<rt>とら</rt></ruby>える",
      "<ruby>障害<rt>しょうがい</rt></ruby>を<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>身<rt>み</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>欠<rt>けつ</rt></ruby><ruby>陥<rt>かん</rt></ruby>としてのみ<ruby>捉<rt>とら</rt></ruby>え、<ruby>環境<rt>かんきょう</rt></ruby>の<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>は<ruby>考<rt>かんが</rt></ruby><ruby>慮<rt>りょ</rt></ruby>しない",
      "<ruby>医<rt>い</rt></ruby><ruby>師<rt>し</rt></ruby>だけが<ruby>使用<rt>しよう</rt></ruby>する<ruby>医<rt>い</rt></ruby><ruby>学<rt>がく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>診<rt>しん</rt></ruby><ruby>断<rt>だん</rt></ruby>の<ruby>基準<rt>きじゅん</rt></ruby>である",
      "<ruby>障害<rt>しょうがい</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>就<rt>しゅう</rt></ruby><ruby>労<rt>ろう</rt></ruby><ruby>能力<rt>のうりょく</rt></ruby>を<ruby>排除<rt>はいじょ</rt></ruby>するための<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby><ruby>法<rt>ほう</rt></ruby>である"
    ],
    "answer": 1,
    "exp": "ICFは<ruby>生活機能<rt>せいかつきのう</rt></ruby>（<ruby>心身機能<rt>しんしんきのう</rt></ruby>・<ruby>活動<rt>かつどう</rt></ruby>・<ruby>参加<rt>さんか</rt></ruby>）と<ruby>背景因子<rt>はいけいいんし</rt></ruby>（<ruby>環境因子<rt>かんきょういんし</rt></ruby>・<ruby>個人因子<rt>こじんいんし</rt></ruby>）の<ruby>相<rt>そう</rt></ruby><ruby>互<rt>たが</rt></ruby><ruby>関係<rt>かんけい</rt></ruby>を<ruby>包<rt>つつ</rt></ruby><ruby>括<rt>かつ</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>捉<rt>とら</rt></ruby>える<ruby>枠組み<rt>わくぐみ</rt></ruby>です。"
  },
  {
    "id": 55,
    "stem": "ICFの<ruby>構<rt>こう</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>要素<rt>ようそ</rt></ruby>のうち、<ruby>家族<rt>かぞく</rt></ruby>、<ruby>住<rt>じゅう</rt></ruby><ruby>宅<rt>たく</rt></ruby><ruby>環境<rt>かんきょう</rt></ruby>、<ruby>福祉用具<rt>ふくしようぐ</rt></ruby>、<ruby>法律<rt>ほうりつ</rt></ruby>・<ruby>社会制度<rt>しゃかいせいど</rt></ruby>などが<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>される<ruby>項<rt>こう</rt></ruby><ruby>目<rt>め</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>心身機能<rt>しんしんきのう</rt></ruby>・<ruby>身体構造<rt>しんたいこうぞう</rt></ruby>",
      "<ruby>環境因子<rt>かんきょういんし</rt></ruby>",
      "<ruby>個人因子<rt>こじんいんし</rt></ruby>",
      "<ruby>健康状態<rt>けんこうじょうたい</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>福祉用具<rt>ふくしようぐ</rt></ruby>や<ruby>建<rt>た</rt></ruby><ruby>物<rt>もの</rt></ruby>の<ruby>構造<rt>こうぞう</rt></ruby>、<ruby>介<rt>かい</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>、<ruby>社会制度<rt>しゃかいせいど</rt></ruby>などの<ruby>外的要因<rt>がいてきよういん</rt></ruby>は「<ruby>環境因子<rt>かんきょういんし</rt></ruby>」に<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>されます。"
  },
  {
    "id": 56,
    "stem": "ICFの<ruby>構<rt>こう</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>要素<rt>ようそ</rt></ruby>のうち、<ruby>年齢<rt>ねんれい</rt></ruby>、<ruby>性別<rt>せいべつ</rt></ruby>、<ruby>価値観<rt>かちかん</rt></ruby>、ライフスタイル、<ruby>生活歴<rt>せいかつれき</rt></ruby>などが<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>される<ruby>項<rt>こう</rt></ruby><ruby>目<rt>め</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>環境因子<rt>かんきょういんし</rt></ruby>",
      "<ruby>個人因子<rt>こじんいんし</rt></ruby>",
      "<ruby>活動<rt>かつどう</rt></ruby>",
      "<ruby>参加<rt>さんか</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>個<rt>こ</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>年齢<rt>ねんれい</rt></ruby>、<ruby>性別<rt>せいべつ</rt></ruby>、<ruby>生活歴<rt>せいかつれき</rt></ruby>、これまでの<ruby>人<rt>ひと</rt></ruby><ruby>生<rt>せい</rt></ruby>で<ruby>培<rt>ばい</rt></ruby>った<ruby>価値観<rt>かちかん</rt></ruby>や<ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby>などは「<ruby>個人因子<rt>こじんいんし</rt></ruby>」に<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>されます。"
  },
  {
    "id": 57,
    "stem": "<ruby>本<rt>ほん</rt></ruby><ruby>人<rt>ひと</rt></ruby>の<ruby>意思決定<rt>いしけってい</rt></ruby>を<ruby>尊重<rt>そんちょう</rt></ruby>し、<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>を<ruby>代<rt>だい</rt></ruby><ruby>弁<rt>べん</rt></ruby>・<ruby>擁<rt>よう</rt></ruby><ruby>護<rt>ご</rt></ruby>する<ruby>支援<rt>しえん</rt></ruby><ruby>姿勢<rt>しせい</rt></ruby>を<ruby>表<rt>ひょう</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>アドボカシー<rt>あどぼかしー</rt></ruby>（<ruby>権利擁護<rt>けんりようご</rt></ruby>）",
      "<ruby>パターナリズム<rt>ぱたーなりずむ</rt></ruby>（<ruby>父権主義<rt>ふけんしゅぎ</rt></ruby>）",
      "インスティテューショナリズム（<ruby>施設症<rt>しせつしょう</rt></ruby>）",
      "スクリーニング"
    ],
    "answer": 1,
    "exp": "<ruby>アドボカシー<rt>あどぼかしー</rt></ruby>とは、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>を<ruby>守<rt>まも</rt></ruby>り、<ruby>自<rt>じ</rt></ruby>らの<ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby>を<ruby>表<rt>ひょう</rt></ruby><ruby>明<rt>あか</rt></ruby>・<ruby>行<rt>こう</rt></ruby><ruby>使<rt>つか</rt></ruby>できるように<ruby>代<rt>だい</rt></ruby><ruby>弁<rt>べん</rt></ruby>・<ruby>支援<rt>しえん</rt></ruby>する<ruby>活動<rt>かつどう</rt></ruby>のことです。"
  },
  {
    "id": 58,
    "stem": "<ruby>本<rt>ほん</rt></ruby><ruby>来<rt>く</rt></ruby>もっている<ruby>能力<rt>のうりょく</rt></ruby>や<ruby>力<rt>ちから</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>で</rt></ruby>し、<ruby>自<rt>じ</rt></ruby>らの<ruby>力<rt>ちから</rt></ruby>で<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>を<ruby>解<rt>かい</rt></ruby><ruby>決<rt>けつ</rt></ruby>していけるよう<ruby>支援<rt>しえん</rt></ruby>する<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>エンパワメント<rt>えんぱわめんと</rt></ruby>",
      "アセスメント",
      "モデリング",
      "<ruby>ラポール<rt>らぽーる</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>エンパワメント<rt>えんぱわめんと</rt></ruby>とは、<ruby>人<rt>ひと</rt></ruby>が<ruby>本<rt>ほん</rt></ruby><ruby>来<rt>く</rt></ruby>もっている<ruby>潜在的な力<rt>せんざいてきなちから</rt></ruby>や<ruby>尊厳<rt>そんげん</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>で</rt></ruby>し、<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>を<ruby>自<rt>じ</rt></ruby>らコントロールする<ruby>力<rt>ちから</rt></ruby>を<ruby>回復<rt>かいふく</rt></ruby>させる<ruby>支援<rt>しえん</rt></ruby>です。"
  },
  {
    "id": 59,
    "stem": "「コミュニケーション（communication）」の<ruby>語源<rt>ごげん</rt></ruby>となったラテン<ruby>語<rt>ご</rt></ruby>（communicare）の<ruby>本<rt>ほん</rt></ruby><ruby>来<rt>く</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>指示<rt>しじ</rt></ruby>・<ruby>命<rt>めい</rt></ruby><ruby>令<rt>れい</rt></ruby>して<ruby>服従<rt>ふくじゅう</rt></ruby>させること",
      "<ruby>分かち合う<rt>わかちあう</rt></ruby>、<ruby>共有<rt>きょうゆう</rt></ruby>する、<ruby>共通項<rt>きょうつうこう</rt></ruby>をつくること",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>行<rt>こう</rt></ruby><ruby>動<rt>どう</rt></ruby>を<ruby>制<rt>せい</rt></ruby><ruby>限<rt>げん</rt></ruby>して<ruby>管<rt>かん</rt></ruby><ruby>理<rt>り</rt></ruby>すること",
      "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>正<rt>せい</rt></ruby>しさを<ruby>論<rt>ろん</rt></ruby><ruby>破<rt>は</rt></ruby>して<ruby>証<rt>しょう</rt></ruby><ruby>明<rt>あか</rt></ruby>すること"
    ],
    "answer": 2,
    "exp": "<ruby>語源<rt>ごげん</rt></ruby>であるラテン<ruby>語<rt>ご</rt></ruby>「コミュニカーレ」は「<ruby>分かち合う<rt>わかちあう</rt></ruby>」「<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby>のものにする」という<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>を<ruby>持<rt>も</rt></ruby>っています。"
  },
  {
    "id": 60,
    "stem": "コミュニケーションを<ruby>構<rt>こう</rt></ruby><ruby>成<rt>せい</rt></ruby>する「<ruby>言語的コミュニケーション<rt>げんごてきこみゅにけーしょん</rt></ruby>」の<ruby>例<rt>れい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>言葉<rt>ことば</rt></ruby>による<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>や<ruby>文字<rt>もじ</rt></ruby>・<ruby>文<rt>ぶん</rt></ruby><ruby>章<rt>しょう</rt></ruby>",
      "<ruby>顔<rt>かお</rt></ruby>の<ruby>表情<rt>ひょうじょう</rt></ruby>やアイコンタクト",
      "<ruby>身<rt>み</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>姿勢<rt>しせい</rt></ruby>やお<ruby>辞<rt>じ</rt></ruby><ruby>儀<rt>ぎ</rt></ruby>",
      "<ruby>声<rt>こえ</rt></ruby>のトーンや<ruby>話<rt>はな</rt></ruby>すスピード"
    ],
    "answer": 1,
    "exp": "<ruby>言葉<rt>ことば</rt></ruby>や<ruby>文字<rt>もじ</rt></ruby>を<ruby>用<rt>よう</rt></ruby>いて<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>を<ruby>伝<rt>つた</rt></ruby>える<ruby>手<rt>て</rt></ruby><ruby>段<rt>だん</rt></ruby>が「<ruby>言語的コミュニケーション<rt>げんごてきこみゅにけーしょん</rt></ruby>」です。"
  },
  {
    "id": 61,
    "stem": "コミュニケーションにおいて<ruby>言葉<rt>ことば</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>外<rt>そと</rt></ruby>の<ruby>手<rt>て</rt></ruby><ruby>段<rt>だん</rt></ruby>で<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>伝<rt>つた</rt></ruby>える「<ruby>非言語的コミュニケーション<rt>ひげんごてきこみゅにけーしょん</rt></ruby>」の<ruby>例<rt>れい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>表情<rt>ひょうじょう</rt></ruby>、<ruby>視線<rt>しせん</rt></ruby>、<ruby>身振り<rt>みぶり</rt></ruby>、<ruby>声<rt>こえ</rt></ruby>の<ruby>調<rt>ちょう</rt></ruby><ruby>子<rt>こ</rt></ruby>、<ruby>身体的距離<rt>しんたいてききょり</rt></ruby>",
      "メールの<ruby>本<rt>ほん</rt></ruby><ruby>文<rt>ぶん</rt></ruby>テキスト",
      "<ruby>手<rt>て</rt></ruby><ruby>書<rt>しょ</rt></ruby>きの<ruby>手<rt>て</rt></ruby><ruby>紙<rt>かみ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby><ruby>章<rt>しょう</rt></ruby>",
      "<ruby>口頭<rt>こうとう</rt></ruby>で<ruby>読<rt>よ</rt></ruby>み<ruby>上<rt>うえ</rt></ruby>げられた<ruby>契約書<rt>けいやくしょ</rt></ruby>の<ruby>条文<rt>じょうぶん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>表情<rt>ひょうじょう</rt></ruby>、<ruby>視線<rt>しせん</rt></ruby>、ジェスチャー、<ruby>姿勢<rt>しせい</rt></ruby>、<ruby>声<rt>こえ</rt></ruby>の<ruby>抑<rt>よく</rt></ruby><ruby>揚<rt>あ</rt></ruby>、<ruby>相手<rt>あいて</rt></ruby>との<ruby>物理的距離<rt>ぶつりてききょり</rt></ruby>などはすべて<ruby>非言語的コミュニケーション<rt>ひげんごてきこみゅにけーしょん</rt></ruby>です。"
  },
  {
    "id": 62,
    "stem": "<ruby>文<rt>ぶん</rt></ruby><ruby>化<rt>か</rt></ruby>や<ruby>集団<rt>しゅうだん</rt></ruby><ruby>内<rt>うち</rt></ruby>で<ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>が<ruby>共有<rt>きょうゆう</rt></ruby>されており、<ruby>言葉<rt>ことば</rt></ruby>の<ruby>代<rt>だい</rt></ruby>わりとして<ruby>使<rt>つか</rt></ruby>われる<ruby>身振り<rt>みぶり</rt></ruby>（OKサインや<ruby>手招き<rt>てまねき</rt></ruby>など）を<ruby>表<rt>ひょう</rt></ruby>す<ruby>非<rt>ひ</rt></ruby><ruby>言語<rt>げんご</rt></ruby><ruby>動作<rt>どうさ</rt></ruby>として<ruby>適切<rt>てきせつ</rt></ruby>なものを<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>表象<rt>ひょうしょう</rt></ruby>（エンブレム）",
      "<ruby>例示<rt>れいじ</rt></ruby>（イラストレーション）",
      "<ruby>適応動作<rt>てきおうどうさ</rt></ruby>（アダプター）",
      "<ruby>調整動作<rt>ちょうせいどうさ</rt></ruby>（レギュレーター）"
    ],
    "answer": 1,
    "exp": "エンブレム（<ruby>表象<rt>ひょうしょう</rt></ruby>）とは、ピースサインやOKサインのように、<ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>言語<rt>げんご</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>味<rt>あじ</rt></ruby>に<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>置<rt>お</rt></ruby>き<ruby>換<rt>かん</rt></ruby>えられる<ruby>動作<rt>どうさ</rt></ruby>のことです。"
  },
  {
    "id": 63,
    "stem": "<ruby>言葉<rt>ことば</rt></ruby>による<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>の<ruby>内<rt>うち</rt></ruby><ruby>容<rt>よう</rt></ruby>を<ruby>強<rt>つよ</rt></ruby><ruby>調<rt>ちょう</rt></ruby>したり<ruby>補<rt>ほ</rt></ruby><ruby>足<rt>あし</rt></ruby>したりするために、<ruby>身振り<rt>みぶり</rt></ruby><ruby>手<rt>て</rt></ruby><ruby>振<rt>ふ</rt></ruby>りで<ruby>大<rt>おお</rt></ruby>きさや<ruby>形<rt>かたち</rt></ruby>を<ruby>示<rt>し</rt></ruby>す<ruby>動作<rt>どうさ</rt></ruby>を<ruby>表<rt>ひょう</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>例示<rt>れいじ</rt></ruby>（イラストレーション）",
      "<ruby>表象<rt>ひょうしょう</rt></ruby>（エンブレム）",
      "<ruby>適応動作<rt>てきおうどうさ</rt></ruby>（アダプター）",
      "<ruby>調整動作<rt>ちょうせいどうさ</rt></ruby>（レギュレーター）"
    ],
    "answer": 1,
    "exp": "<ruby>話<rt>はな</rt></ruby>の<ruby>内<rt>うち</rt></ruby><ruby>容<rt>よう</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせて「これくらい<ruby>大<rt>おお</rt></ruby>きい」と<ruby>手<rt>て</rt></ruby>で<ruby>形<rt>かたち</rt></ruby>を<ruby>示<rt>し</rt></ruby>すような<ruby>動作<rt>どうさ</rt></ruby>はイラストレーション（<ruby>例示<rt>れいじ</rt></ruby>）と<ruby>呼<rt>よ</rt></ruby>ばれます。"
  },
  {
    "id": 64,
    "stem": "<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>の<ruby>聞き手<rt>ききて</rt></ruby>が「うなずき」や「<ruby>相づち<rt>あいづち</rt></ruby>」を<ruby>打<rt>う</rt></ruby>つことで、<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>の<ruby>流<rt>なが</rt></ruby>れを<ruby>円<rt>えん</rt></ruby><ruby>滑<rt>かつ</rt></ruby>に<ruby>進<rt>しん</rt></ruby>めたり<ruby>発<rt>はつ</rt></ruby><ruby>言<rt>げん</rt></ruby>を<ruby>促<rt>うなが</rt></ruby>したりする<ruby>動作<rt>どうさ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>調整動作<rt>ちょうせいどうさ</rt></ruby>（レギュレーター）",
      "<ruby>適応動作<rt>てきおうどうさ</rt></ruby>（アダプター）",
      "<ruby>表象<rt>ひょうしょう</rt></ruby>（エンブレム）",
      "<ruby>感情表出動作<rt>かんじょうひょうしゅつどうさ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>相づち<rt>あいづち</rt></ruby>やうなずき、<ruby>視線<rt>しせん</rt></ruby>の<ruby>移動<rt>いどう</rt></ruby>など、<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>のやり<ruby>取<rt>と</rt></ruby>りをコントロール・<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby>する<ruby>動作<rt>どうさ</rt></ruby>をレギュレーター（<ruby>調整動作<rt>ちょうせいどうさ</rt></ruby>）といいます。"
  },
  {
    "id": 65,
    "stem": "<ruby>緊<rt>きん</rt></ruby><ruby>張<rt>は</rt></ruby>や<ruby>不<rt>ふ</rt></ruby><ruby>安<rt>あん</rt></ruby>を<ruby>感<rt>かん</rt></ruby>じたときに、<ruby>無意識<rt>むいしき</rt></ruby>に<ruby>髪<rt>かみ</rt></ruby>を<ruby>触<rt>ふ</rt></ruby>ったり<ruby>手<rt>て</rt></ruby>をもんだりして<ruby>心<rt>こころ</rt></ruby>の<ruby>安<rt>あん</rt></ruby><ruby>定<rt>てい</rt></ruby>を<ruby>図<rt>ず</rt></ruby>る<ruby>動作<rt>どうさ</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>適応動作<rt>てきおうどうさ</rt></ruby>（アダプター）",
      "<ruby>調整動作<rt>ちょうせいどうさ</rt></ruby>（レギュレーター）",
      "<ruby>表象<rt>ひょうしょう</rt></ruby>（エンブレム）",
      "<ruby>例示<rt>れいじ</rt></ruby>（イラストレーション）"
    ],
    "answer": 1,
    "exp": "<ruby>不<rt>ふ</rt></ruby><ruby>安<rt>あん</rt></ruby>や<ruby>退<rt>たい</rt></ruby><ruby>屈<rt>くつ</rt></ruby>、ストレスなどを<ruby>和<rt>わ</rt></ruby>らげるために<ruby>無意識<rt>むいしき</rt></ruby>に<ruby>行<rt>こう</rt></ruby>われる<ruby>自己接触<rt>じこせっしょく</rt></ruby>などの<ruby>動作<rt>どうさ</rt></ruby>をアダプター（<ruby>適応動作<rt>てきおうどうさ</rt></ruby>）といいます。"
  },
  {
    "id": 66,
    "stem": "エドワード・ホールの<ruby>対人距離<rt>たいじんきょり</rt></ruby>の<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>において、<ruby>家族<rt>かぞく</rt></ruby>や<ruby>恋<rt>こい</rt></ruby><ruby>人<rt>ひと</rt></ruby>などごく<ruby>親<rt>おや</rt></ruby>しい<ruby>関係<rt>かんけい</rt></ruby>で<ruby>用<rt>よう</rt></ruby>いられる<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>はな</rt></ruby>（0〜50cm）として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>密接距離<rt>みっせつきょり</rt></ruby>",
      "<ruby>個人の距離<rt>こじんのきょり</rt></ruby>",
      "<ruby>社会的な距離<rt>しゃかいてきなきょり</rt></ruby>",
      "<ruby>公的な距離<rt>こうてきなきょり</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>密接距離<rt>みっせつきょり</rt></ruby>（0〜50cm）は、<ruby>身<rt>み</rt></ruby><ruby>体<rt>たい</rt></ruby>が<ruby>触<rt>ふ</rt></ruby>れ<ruby>合<rt>あ</rt></ruby>うほど<ruby>親密<rt>しんみつ</rt></ruby>な<ruby>間<rt>あいだ</rt></ruby><ruby>柄<rt>がら</rt></ruby>で<ruby>用<rt>よう</rt></ruby>いられる<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>はな</rt></ruby><ruby>帯<rt>おび</rt></ruby>です。"
  },
  {
    "id": 67,
    "stem": "エドワード・ホールの<ruby>対人距離<rt>たいじんきょり</rt></ruby>の<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>において、<ruby>日<rt>ひ</rt></ruby><ruby>常<rt>じょう</rt></ruby>の<ruby>友<rt>とも</rt></ruby><ruby>人<rt>ひと</rt></ruby>や<ruby>同僚<rt>どうりょう</rt></ruby>との<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>に<ruby>適<rt>てき</rt></ruby>した<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>はな</rt></ruby>（<ruby>約<rt>やく</rt></ruby>50cm〜120cm）として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>個人の距離<rt>こじんのきょり</rt></ruby>（<ruby>個体的距離<rt>こたいてききょり</rt></ruby>）",
      "<ruby>密接距離<rt>みっせつきょり</rt></ruby>",
      "<ruby>公的な距離<rt>こうてきなきょり</rt></ruby>",
      "<ruby>遠隔距離<rt>えんかくきょり</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>個人の距離<rt>こじんのきょり</rt></ruby>（<ruby>約<rt>やく</rt></ruby>50〜120cm）は、<ruby>手<rt>て</rt></ruby>を<ruby>伸<rt>の</rt></ruby>ばせば<ruby>触<rt>ふ</rt></ruby>れられる<ruby>程<rt>てい</rt></ruby><ruby>度<rt>ど</rt></ruby>で、<ruby>個人的<rt>こじんてき</rt></ruby>な<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はな</rt></ruby>を<ruby>交<rt>こう</rt></ruby>わすのに<ruby>適<rt>てき</rt></ruby>した<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>はな</rt></ruby><ruby>帯<rt>おび</rt></ruby>です。"
  },
  {
    "id": 68,
    "stem": "<ruby>相手<rt>あいて</rt></ruby>の<ruby>話<rt>はな</rt></ruby>を<ruby>聴<rt>ちょう</rt></ruby>く「<ruby>傾聴<rt>けいちょう</rt></ruby>（アクティブリスニング）」の<ruby>基本姿勢<rt>きほんしせい</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>途<rt>と</rt></ruby><ruby>中<rt>なか</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>言<rt>げん</rt></ruby>を<ruby>遮<rt>しゃ</rt></ruby>って、<ruby>援助者<rt>えんじょしゃ</rt></ruby>の<ruby>正論<rt>せいろん</rt></ruby>やアドバイスを<ruby>一<rt>いち</rt></ruby><ruby>方<rt>かた</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>話<rt>はな</rt></ruby>し<ruby>続<rt>ぞく</rt></ruby>ける",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>目<rt>め</rt></ruby>や<ruby>表情<rt>ひょうじょう</rt></ruby>に<ruby>注<rt>ちゅう</rt></ruby><ruby>意<rt>い</rt></ruby>を<ruby>向<rt>む</rt></ruby>け、<ruby>受容的<rt>じゅようてき</rt></ruby>な<ruby>相づち<rt>あいづち</rt></ruby>を<ruby>打<rt>う</rt></ruby>ちながら<ruby>気持ち<rt>きもち</rt></ruby>に<ruby>寄<rt>よ</rt></ruby>り<ruby>添<rt>そ</rt></ruby>って<ruby>聴<rt>ちょう</rt></ruby>く",
      "<ruby>腕<rt>うで</rt></ruby><ruby>組<rt>くみ</rt></ruby>みをして<ruby>腕<rt>うで</rt></ruby>や<ruby>脚<rt>あし</rt></ruby>を<ruby>組<rt>くみ</rt></ruby>み<ruby>替<rt>か</rt></ruby>えながら、<ruby>時<rt>とき</rt></ruby><ruby>計<rt>けい</rt></ruby>を<ruby>頻<rt>ひん</rt></ruby><ruby>繁<rt>はん</rt></ruby>に<ruby>気<rt>き</rt></ruby>にして<ruby>聴<rt>ちょう</rt></ruby>く",
      "<ruby>相手<rt>あいて</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>の<ruby>起<rt>お</rt></ruby><ruby>伏<rt>ふく</rt></ruby>を<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>し、「そんなことで<ruby>悩<rt>なや</rt></ruby>むのは<ruby>無<rt>む</rt></ruby><ruby>駄<rt>だ</rt></ruby>だ」と<ruby>諭<rt>ゆ</rt></ruby>す"
    ],
    "answer": 2,
    "exp": "<ruby>傾聴<rt>けいちょう</rt></ruby>とは、<ruby>相手<rt>あいて</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>だけでなく<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>表情<rt>ひょうじょう</rt></ruby>に<ruby>心<rt>こころ</rt></ruby>を<ruby>傾<rt>かたむ</rt></ruby>け、<ruby>受容<rt>じゅよう</rt></ruby>と<ruby>共感<rt>きょうかん</rt></ruby>の<ruby>姿勢<rt>しせい</rt></ruby>をもって<ruby>最<rt>もっと</rt></ruby><ruby>後<rt>あと</rt></ruby>まで<ruby>真<rt>ま</rt></ruby><ruby>摯<rt>し</rt></ruby>に<ruby>聴<rt>ちょう</rt></ruby>く<ruby>技<rt>ぎ</rt></ruby><ruby>術<rt>じゅつ</rt></ruby>です。"
  },
  {
    "id": 69,
    "stem": "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>や<ruby>意<rt>い</rt></ruby><ruby>見<rt>み</rt></ruby>を<ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>は</rt></ruby>すると<ruby>同<rt>おな</rt></ruby><ruby>時<rt>とき</rt></ruby>に、<ruby>相手<rt>あいて</rt></ruby>の<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>や<ruby>思<rt>おも</rt></ruby>いも<ruby>大切<rt>たいせつ</rt></ruby>にして<ruby>対<rt>たい</rt></ruby><ruby>等<rt>とう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>わる<ruby>自己表現法<rt>じこひょうげんほう</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "アサーティブ・コミュニケーション",
      "アグレッシブ（<ruby>攻<rt>こう</rt></ruby><ruby>撃<rt>げき</rt></ruby><ruby>的<rt>てき</rt></ruby>）コミュニケーション",
      "ノンアサーティブ（<ruby>非<rt>ひ</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>は</rt></ruby><ruby>的<rt>てき</rt></ruby>）コミュニケーション",
      "<ruby>操<rt>そう</rt></ruby><ruby>作<rt>つく</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション"
    ],
    "answer": 1,
    "exp": "アサーティブとは、<ruby>自分<rt>じぶん</rt></ruby>を<ruby>卑<rt>ひ</rt></ruby><ruby>下<rt>した</rt></ruby>することも<ruby>相手<rt>あいて</rt></ruby>を<ruby>攻<rt>こう</rt></ruby><ruby>撃<rt>げき</rt></ruby>することもなく、<ruby>相互尊重<rt>そうごそんちょう</rt></ruby>の<ruby>立<rt>た</rt></ruby><ruby>場<rt>ば</rt></ruby>で<ruby>率直<rt>そっちょく</rt></ruby>に<ruby>想<rt>そう</rt></ruby>いを<ruby>伝<rt>つた</rt></ruby>える<ruby>姿勢<rt>しせい</rt></ruby>です。"
  },
  {
    "id": 70,
    "stem": "<ruby>介護<rt>かいご</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>場<rt>ば</rt></ruby>におけるコミュニケーションの<ruby>最終的な目標<rt>さいしゅうてきなもくてき</rt></ruby>として<ruby>最も適切なもの<rt>もっともてきせつなもの</rt></ruby>を1つ<ruby>選びなさい<rt>えらびなさい</rt></ruby>。",
    "options": [
      "<ruby>介護<rt>かいご</rt></ruby><ruby>職<rt>しょく</rt></ruby>が<ruby>指示<rt>しじ</rt></ruby><ruby>通<rt>つう</rt></ruby>りに<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>を<ruby>動<rt>どう</rt></ruby>かすための<ruby>主導権<rt>しゅどうけん</rt></ruby>を<ruby>確<rt>かく</rt></ruby><ruby>保<rt>ほ</rt></ruby>すること",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>安<rt>あん</rt></ruby><ruby>心<rt>こころ</rt></ruby><ruby>感<rt>かん</rt></ruby>をもち、<ruby>意思や希望<rt>いしやきぼう</rt></ruby>を<ruby>主体<rt>しゅたい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>表<rt>ひょう</rt></ruby><ruby>明<rt>あか</rt></ruby>してその<ruby>人<rt>ひと</rt></ruby>らしく<ruby>生<rt>せい</rt></ruby>きられる<ruby>関係<rt>かんけい</rt></ruby>を<ruby>築<rt>ちく</rt></ruby>くこと",
      "<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>の<ruby>報<rt>ほう</rt></ruby><ruby>告<rt>こく</rt></ruby><ruby>事<rt>こと</rt></ruby><ruby>項<rt>こう</rt></ruby>だけを<ruby>事<rt>こと</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>伝<rt>つた</rt></ruby><ruby>達<rt>たつ</rt></ruby>し、<ruby>個人的<rt>こじんてき</rt></ruby>な<ruby>関<rt>かん</rt></ruby>わりを<ruby>一<rt>いち</rt></ruby><ruby>切<rt>き</rt></ruby><ruby>排除<rt>はいじょ</rt></ruby>すること",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>要<rt>よう</rt></ruby><ruby>求<rt>もと</rt></ruby>をすべて<ruby>断<rt>だん</rt></ruby>り、<ruby>施設<rt>しせつ</rt></ruby><ruby>側<rt>がわ</rt></ruby>の<ruby>規<rt>き</rt></ruby><ruby>則<rt>そく</rt></ruby>を<ruby>完<rt>かん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>に<ruby>遵守<rt>じゅんしゅ</rt></ruby>させること"
    ],
    "answer": 2,
    "exp": "<ruby>介護<rt>かいご</rt></ruby>におけるコミュニケーションは、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>尊厳<rt>そんげん</rt></ruby>を<ruby>守<rt>まも</rt></ruby>り、<ruby>意思決定<rt>いしけってい</rt></ruby>と<ruby>自己実現<rt>じこじつげん</rt></ruby>を<ruby>支<rt>し</rt></ruby>える<ruby>パートナーシップ<rt>ぱーとなーしっぷ</rt></ruby>を<ruby>築<rt>ちく</rt></ruby>くためにあります。"
  }
]

# セッション状態の初期化
for q in QUESTIONS:
    key = f"ans_{q['id']}"
    if key not in st.session_state:
        st.session_state[key] = None

# 表示モード選択（全問一括 or 10問ずつ分割）
st.markdown("<div class='nav-box'>", unsafe_allow_html=True)
view_mode = st.radio(
    "📖 出題の表示方法を選択してください:",
    options=["10問ずつ分割表示（推奨）", "全70問を一括表示"],
    horizontal=True
)

if view_mode == "10問ずつ分割表示（推奨）":
    batch_options = [
        "第 1問 〜 第10問 （人類の進化とケアの起源）",
        "第11問 〜 第20問 （初期人類・ケアの象徴と自己理解）",
        "第21問 〜 第30問 （先天的・後天的要素とジョハリの窓）",
        "第31問 〜 第40問 （自己覚知・自己開示・ラポール）",
        "第41問 〜 第50問 （変化の可能性・多様性と人間の尊厳）",
        "第51問 〜 第60問 （福祉理念・自立の多面性とICF）",
        "第61問 〜 第70問 （コミュニケーション技術と対人距離）"
    ]
    selected_batch = st.selectbox("取り組む問題群を選択してください:", batch_options)
    batch_idx = batch_options.index(selected_batch)
    start_i = batch_idx * 10
    end_i = start_i + 10
    display_questions = QUESTIONS[start_i:end_i]
else:
    display_questions = QUESTIONS
st.markdown("</div>", unsafe_allow_html=True)

# 解答進捗バー
answered_count = sum(1 for q in QUESTIONS if st.session_state.get(f"ans_{q['id']}") is not None)
st.progress(answered_count / len(QUESTIONS))
st.caption(f"現在の解答進捗: {answered_count} / {len(QUESTIONS)} 問 完了")

# 問題表示と解答入力
for q in display_questions:
    q_num = q["id"]
    key = f"ans_{q_num}"
    
    st.markdown("<div class='q-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='q-title'>第 {q_num} 問. {q['stem']}</div>", unsafe_allow_html=True)
    
    for opt_idx, opt in enumerate(q["options"]):
        st.markdown(f"<div class='opt-item'>{opt_idx + 1}. {opt}</div>", unsafe_allow_html=True)
        
    cur_val = st.session_state.get(key)
    selected_val = st.radio(
        label=f"第 {q_num} 問の解答を選択:",
        options=[1, 2, 3, 4],
        index=[1, 2, 3, 4].index(cur_val) if cur_val in [1, 2, 3, 4] else None,
        horizontal=True,
        key=f"radio_{q_num}"
    )
    if selected_val is not None:
        st.session_state[key] = selected_val
    st.markdown("</div>", unsafe_allow_html=True)

# 採点と提出用テキストの生成
st.markdown("---")
if st.button("📊 採点して提出用テキストを作成する", type="primary", use_container_width=True):
    if not s_class.strip() or not s_id.strip() or not s_name.strip():
        st.error("⚠️ 「クラス名」「学籍番号」「名前」をすべて入力してください。")
    else:
        score = 0
        unanswered = 0
        detail_lines = []
        
        for q in QUESTIONS:
            q_num = q["id"]
            u_ans = st.session_state.get(f"ans_{q_num}")
            is_correct = (u_ans == q["answer"])
            
            if u_ans is None:
                unanswered += 1
                status_str = "未回答 ×"
                ans_str = "未"
            elif is_correct:
                score += 1
                status_str = "正解 ○"
                ans_str = str(u_ans)
            else:
                status_str = "不正解 ×"
                ans_str = str(u_ans)
                
            detail_lines.append(f"問{q_num:02d}: あなたの解答 [{ans_str}] / 正解 [{q['answer']}] -> {status_str}")
            
        total_q = len(QUESTIONS)
        pct = round((score / total_q) * 100)
        
        st.markdown(f"""
        <div class='score-badge'>
          <h3 style='margin:0 0 8px 0; color:#1e3a8a;'>採点結果（人間関係とコミュニケーション a前半）</h3>
          <div style='font-size: 2.2rem; font-weight: bold; color: #1e3a8a;'>{score} / {total_q} 点</div>
          <div style='font-size: 1.1rem; color: #475569;'>正答率: <strong>{pct}%</strong></div>
        </div>
        """, unsafe_allow_html=True)
        
        if unanswered > 0:
            st.warning(f"※ 未回答の問題が {unanswered} 問あります。")
            
        # 解説アコーディオン
        with st.expander("📖 各問題の正解と解説を確認する"):
            for q in QUESTIONS:
                st.markdown(f"**第 {q['id']} 問**")
                st.markdown(f"・{q['exp']}", unsafe_allow_html=True)
                st.markdown("---")
                
        # 提出用テキストの構築
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y年%m月%d日 %H:%M:%S")
        auth_raw = f"{s_class}_{s_id}_{s_name}_{score}_{total_q}_{timestamp}"
        auth_code = f"VER-C2A70-{abs(hash(auth_raw)):X}-{now.strftime('%f')}"
        
        details_block = "\n".join(detail_lines)
        report_text = (
            "==================================================\n"
            "【課題提出用 成績レポート（全70問）】\n"
            "教科・単元　：人間関係とコミュニケーション a前半\n"
            f"クラス名（組）：{s_class.strip()}\n"
            f"学籍番号　　：{s_id.strip()}\n"
            f"名前（氏名）：{s_name.strip()}\n"
            f"実施日時　　：{timestamp}\n"
            f"得点　　　　：{score} / {total_q} 点（正答率 {pct}%）\n"
            f"改ざん防止用認証コード：{auth_code}\n"
            "==================================================\n"
            "【全70問の解答記録】\n"
            f"{details_block}\n"
            "==================================================\n"
            "以上を提出内容として記録しました。\n"
        )
        
        st.markdown("### 📥 課題の提出方法（2通りの方法が使えます）")
        st.info("""
**【提出方法A：テキストファイルをダウンロードして提出】**
1. すぐ下の **「📥 提出用テキストファイル（.txt）をダウンロード」** ボタンを押してファイルを端末に保存します。
2. Google Classroom の該当課題ページで **「ファイルの添付」** から保存したテキストファイルを提出してください。

**【提出方法B：テキストをコピー＆ペーストして提出】**
1. さらに下にある **「📋 コピーペースト用提出テキスト」** の枠内をクリックし、すべて選択（Ctrl+A / ⌘+A）してコピーします。
2. Google Classroom の回答欄・コメント欄にそのまま貼り付けて提出してください。
""")
        
        file_name = f"提出用_人間関係とコミュニケーションa前半_70問_{s_class.strip()}_{s_id.strip()}_{s_name.strip()}.txt"
        st.download_button(
            label="📥 提出用テキストファイル（.txt）をダウンロード",
            data=report_text,
            file_name=file_name,
            mime="text/plain",
            use_container_width=True
        )
        
        st.markdown("<div style='margin-top:14px;'></div>", unsafe_allow_html=True)
        
        st.text_area(
            label="📋 コピーペースト用提出テキスト（枠内をすべて選択・コピーしてGoogle Classroomに貼り付け）:",
            value=report_text,
            height=280
        )
        
        st.markdown("[Google Classroom を開く ↗](https://classroom.google.com)", unsafe_allow_html=True)
