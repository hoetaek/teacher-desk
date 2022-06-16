<template >
  <div style="width: 246.32px; height: 635.56px;">
    <div class="
    tile
    is-ancestor">
      <div
        class="tile is-parent"
        style="width: 246.32px; height: 381.23px;"
      >
        <article class="tile is-child notification has-background-grey-lighter is-rounded width:246">
          image
        </article>
      </div>
    </div>

    <div
      @click="$router.push('/wordsearch')"
      @mouseover="isHover=true"
      @mouseleave="isHover=false"
      style="cursor: pointer"
      :class="classObject"
    >낱말 찾기</div>
    <div class="has-text-centered">주어진 낱말을
      여러 낱말들 속에서
      찾으며 주요 낱말을
      학습할 수 있는 활동지입니다. </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isHover: false,
    };
  },
  computed: {
    classObject: function () {
      return {
        "title size-is-3 has-text-centered": true,
        "has-text-link": this.isHover,
        "is-underlined": this.isHover,
      };
    },
  },
};
</script>
