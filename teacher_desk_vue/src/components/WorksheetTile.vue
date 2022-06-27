<template >
  <div>
    <div class="card">
      <div class="container p-4">
        <div class="card-image">
          <figure class="image is-square">
            <img
              src="../assets/wordsearch_image.png"
              alt="Image"
            >
          </figure>
        </div>
      </div>
      <div class="card-content">

        <div class="content">
          <h1
            class="title has-text-left"
            @click="$router.push('/wordsearch')"
            @mouseover="isHover=true"
            @mouseleave="isHover=false"
            style="cursor: pointer"
            :class="classObject"
          >낱말 찾기</h1>
          <span class="subtitle is-4">주어진 낱말에서 학습할 낱말 찾기</span>
          <br>
          <div class="level">
            <div class="level-item level-right">
              <div class="icon is-medium">
                <i class="fas fa-heart"></i>
              </div>
              <span>10</span>

            </div>

          </div>
        </div>
      </div>
    </div>

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

<style>
.card {
  box-shadow: none;
  border: solid 3px;
  border-radius: 20px;
}

.icon {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>