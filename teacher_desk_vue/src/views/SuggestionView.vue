<template>
  <div class="suggestions">
    <section class="section has-text-centered">
      <div class="title is-2">반복적으로 만들고 있는 <br>
        활동지나 학습자료가 있나요?</div>
      <p class="title is-2 has-text-info">저희가 대신 만들어드릴게요!</p>

      <div
        class="px-5"
        style="width:50%; border: solid 1px; border-radius: 25px; margin: auto;"
      >
        <textarea
          class="textarea is-medium"
          placeholder="이런 걸 만들어주면 좋겠어요."
        ></textarea>
        <div class="box has-text-right">
          <button
            class="button is-info"
            @click="$router.push('/worksheet')"
          > <span class="icon">
              <i class="fas fa-plus"></i>
            </span><span>남기기</span>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>
<style>
.textarea {
  border: none;
}

.box {
  box-shadow: none;
}
</style>