<template>
  <div class="section">
    <div class="columns is-variable is-8">
      <div class="column">
        <worksheet-tile
          :filename="wordsearchPath"
          :liked="true"
        >
          <template #title>
            낱말 찾기
          </template>
          <template #description>
            주어진 낱말에서 학습할 낱말 찾기
          </template>
          <template #heartNum>
            10
          </template>
        </worksheet-tile>
      </div>
      <div class="column">
        <worksheet-tile
          :filename="wordsearchPath"
          :liked="false"
          :isNotReady="true"
        ><template #title>

            말판 놀이
          </template>
          <template #description>
            주사위를 굴러 먼저 도착하기
          </template>
          <template #heartNum>
            7
          </template>
        </worksheet-tile>
      </div>
      <div class="column">
        <worksheet-tile
          :filename="wordsearchPath"
          :liked="false"
          :isNotReady="true"
        ><template #title>
            도블
          </template>
          <template #description>
            같은 것 먼저 외치기
          </template>
          <template #heartNum>
            20
          </template>
        </worksheet-tile>
      </div>

    </div>

  </div>
</template>
<script>
import WorksheetTile from "@/components/WorksheetTile.vue";
export default {
  data() {
    return {
      wordsearchPath: "wordsearch_image.png",
    };
  },
  components: { WorksheetTile },
};
</script>
