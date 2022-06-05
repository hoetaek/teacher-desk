<template>
  <section class="section">

    <div class="title is-3">01 아이들이 찾게 될 낱말</div>

    <div class="mx-6 mb-6">

      <div class="title is-4 has-text-grey-light">아래에 낱말을 입력해주세요. (모두 안채워도 괜찮아요!)</div>
      <form
        class="has-text-centered"
        method="get"
      >
        <enter-word :words="words"></enter-word>
      </form>
    </div>
    <div class="title is-3">02 문제 옵션</div>
    <div class="mx-6 mb-6">
      <div class="title is-4 has-text-grey-light">원하는 옵션을 선택해주세요.</div>

      <div class="columns is-vcentered">
        <div class="column is-size-4 has-text-weight-bold">
          난이도
        </div>
        <selection-buttons
          :button_infos="difficulty_options"
          :selected_data="difficulty"
          @buttonSeletedEvent="selectDifficulty"
        ></selection-buttons>
      </div>

      <div class="columns is-vcentered">
        <div class="column is-size-4 has-text-weight-bold">
          대소문자 선택하기
        </div>
        <selection-buttons
          :button_infos="alphabetCaseOptions"
          :selected_data="alphabetCase"
          @buttonSeletedEvent="selectAlphabetCase"
        >
          <div class="tile is-parent">
          </div>
        </selection-buttons>

      </div>
      <div class="columns is-vcentered">
        <div class="column is-size-4 has-text-weight-bold">
          찾는 낱말의 철자 순서 섞기 (Scramble)
        </div>
        <div class="column">
          <selection-buttons
            :button_infos="isScrambledOptions"
            :selected_data="isScrambled"
            @buttonSeletedEvent="selectIsScrambled"
          >
            <div class="tile is-parent">
            </div>
          </selection-buttons>
        </div>
      </div>
      <button
        type="submit"
        class="button is-info is-fullwidth is-size-1 has-text-weight-bold"
        id="make-worksheet"
      >
        클릭하여 한글 파일로 다운로드 하기
      </button>
    </div>
  </section>
</template>


<script>
import EnterWord from "@/components/EnterWord.vue";
import SelectionButtons from "@/components/SelectionButtons/SelectionButtons.vue";
export default {
  components: { EnterWord, SelectionButtons },
  data() {
    return {
      words: [],
      difficulty_options: [
        {
          name: "쉬움",
          value: "easy",
        },
        {
          name: "보통",
          value: "normal",
        },
        {
          name: "어려움",
          value: "difficult",
        },
      ],
      alphabetCaseOptions: [
        {
          name: "소문자",
          value: "undercase",
        },
        {
          name: "대문자",
          value: "uppercase",
        },
      ],
      isScrambledOptions: [
        {
          name: "예",
          value: "scrambled",
        },
        {
          name: "아니오",
          value: "notScrambled",
        },
      ],
      difficulty: "easy",
      alphabetCase: "undercase",
      isScrambled: "notScrambled",
    };
  },
  methods: {
    selectDifficulty(selectedValue) {
      this.difficulty = selectedValue;
    },
    selectAlphabetCase(selectedValue) {
      this.alphabetCase = selectedValue;
    },
    selectIsScrambled(selectedValue) {
      this.isScrambled = selectedValue;
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
