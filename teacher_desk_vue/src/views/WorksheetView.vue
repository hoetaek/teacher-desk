<template>
  <div class="section">
    <div class="columns is-variable is-8">
      <div
        class="column"
        v-for="(worksheet, index) in worksheetData"
        :key="index"
      >
        <worksheet-tile
          :filename="worksheet.filename"
          :liked="worksheet.liked"
          :isNotReady="worksheet.isNotReady"
        >
          <template #title>
            {{ worksheet.title }}
          </template>
          <template #description>
            {{ worksheet.description }}
          </template>
          <template #heartNum>
            {{ worksheet.heartNum }}
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
      worksheetData: [
        {
          filename: "wordsearch_image.png",
          liked: true,
          isNotReady: false,
          title: "낱말 찾기",
          description: "주어진 낱말에서 학습할 낱말 찾기",
          heartNum: 10,
        },
        {
          filename: "wordsearch_image.png",
          liked: true,
          isNotReady: true,
          title: "말판 놀이",
          description: "주사위를 굴러 먼저 도착하기",
          heartNum: 7,
        },
        {
          filename: "wordsearch_image.png",
          liked: true,
          isNotReady: true,
          title: "도블",
          description: "같은 것 먼저 외치기",
          heartNum: 20,
        },
      ],
      wordsearchPath: "wordsearch_image.png",
    };
  },
  components: { WorksheetTile },
};
</script>
