<template>
  <section class="section">
    <div class="title is-size-3-desktop is-size-4-mobile">01 아이들이 찾게 될 낱말</div>

    <div class="mx-6 mb-6">

      <div class="title is-size-4-desktop is-size-5-tablet is-size-5-mobile has-text-grey-light">아래에 낱말을 입력해주세요. (모두 안채워도 괜찮아요!)</div>

      <enter-word
        @text-input-changed="firstTextInputChanged"
        :validate-regex='/^[가-힣]+$/'
      ></enter-word>
      <enter-word
        @text-input-changed="secondTextInputChanged"
        :validate-regex='/^[가-힣]+$/'
      ></enter-word>
      <enter-word
        @text-input-changed="thirdTextInputChanged"
        :validate-regex='/^[가-힣]+$/'
      ></enter-word>

    </div>
    <div class="title is-size-3-desktop is-size-4-mobile">02 문제 옵션</div>
    <div class="mx-6 mb-6">
      <div class="title is-size-4-desktop is-size-5-tablet is-size-5-mobile has-text-grey-light">원하는 옵션을 선택해주세요.</div>

      <div class="columns is-vcentered">
        <div class="column is-size-4-desktop is-size-4-tablet is-size-5-mobile has-text-weight-bold">
          난이도
        </div>
        <selection-buttons
          :button_infos="difficulty_options"
          :selected_data="difficulty"
          @button-seleted-event="selectDifficulty"
        ></selection-buttons>
      </div>

      <div class="columns is-vcentered">
        <div class="column is-size-4-desktop is-size-4-tablet is-size-5-mobile has-text-weight-bold">
          초성 힌트 제공
        </div>
        <div class="column">
          <selection-buttons
            :button_infos="isScrambledOptions"
            :selected_data="isScrambled"
            @button-seleted-event="selectIsScrambled"
          >
            <div class="tile is-parent">
            </div>
          </selection-buttons>
        </div>
      </div>
      <button
        type="submit"
        class="button is-info is-fullwidth is-size-2-desktop is-size-4-tablet is-size-6-mobile has-text-weight-bold"
        id="make-worksheet"
        @click="fetchWorksheet"
      >
        클릭하여 한글 파일로 다운로드 하기
      </button>
    </div>
  </section>
</template>


<script>
import EnterWord from "@/components/EnterWord.vue";
import SelectionButtons from "@/components/SelectionButtons/SelectionButtons.vue";
import axios from "axios";
import fileDownload from "js-file-download";

export default {
  components: { EnterWord, SelectionButtons },
  data() {
    return {
      first_row_texts: ["", "", "", "", ""],
      second_row_texts: ["", "", "", "", ""],
      third_row_texts: ["", "", "", "", ""],
      difficulty_options: [
        {
          name: "쉬움",
          value: "EASY",
        },
        {
          name: "보통",
          value: "NORMAL",
        },
        {
          name: "어려움",
          value: "DIFFICULT",
        },
      ],
      isScrambledOptions: [
        {
          name: "예",
          value: true,
        },
        {
          name: "아니오",
          value: false,
        },
      ],
      difficulty: "EASY",
      alphabetCase: false,
      isScrambled: false,
    };
  },
  computed: {
    words() {
      return [
        ...this.first_row_texts,
        ...this.second_row_texts,
        ...this.third_row_texts,
      ];
    },
  },
  methods: {
    selectDifficulty(selectedValue) {
      this.difficulty = selectedValue;
    },
    selectIsScrambled(selectedValue) {
      this.isScrambled = selectedValue;
    },
    firstTextInputChanged(word_array) {
      this.first_row_texts = word_array;
      console.log(this.words);
    },
    secondTextInputChanged(word_array) {
      this.second_row_texts = word_array;
      console.log(this.words);
    },
    thirdTextInputChanged(word_array) {
      this.third_row_texts = word_array;
      console.log(this.words);
    },
    fetchWorksheet: function () {
      let words = this.words.filter((n) => n);
      if (words == 0) return;
      var params = new URLSearchParams();

      for (const word of this.words) {
        params.append("words", word);
      }

      params.append("difficulty", this.difficulty);
      params.append("is_uppercase", false);
      params.append("is_hint_twist", this.isScrambled);

      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/wordsearch",
        params: params,
        responseType: "blob",
        config: {
          headers: {
            Accept:
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "Access-Control-Allow-Origin": "http://localhost:8080",
            "Content-Type":
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
          },
        },
      }).then(function (response) {
        let fileName = "낱말찾기퍼즐.hwp";
        fileDownload(response.data, fileName);
      });
    },
  },
};
</script>

<style scoped lang="scss">
#make-worksheet {
  border-radius: 0px;
}

.tile.is-child {
  padding: 10px;
}
</style>
