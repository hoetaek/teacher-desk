<template>
    <section class="section">


        <div class="title is-3">01 아이들이 찾게 될 낱말</div>


        <div class="mx-6 mb-6">

            <div class="title is-4 has-text-grey-light">아래에 낱말을 입력해주세요. (모두 안채워도 괜찮아요!)</div>
            <form class="has-text-centered" method="get">
                <div class="tile is-ancestor">
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                </div>
                <div class="tile is-ancestor">
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                    <div class="tile is-parent">
                        <article class="tile is-child notification has-background-grey-lighter is-rounded">
                            <input class="input is-static center-block" type="text" placeholder="단어">
                        </article>
                    </div>
                </div>
            </form>
        </div>
        <div class="title is-3">02 문제 옵션</div>
        <div class="mx-6 mb-6">
            <div class="title is-4 has-text-grey-light">원하는 옵션을 선택해주세요.</div>
            <div class="columns is-vcentered">
                <div class="column is-size-4 has-text-weight-bold">
                    난이도
                </div>
                <div class="column">
                    <div class="tile is-ancestor">
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4-desktop is-size-5-tablet is-size-6-mobile has-text-weight-bold">
                                쉬움
                            </button>
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4-desktop is-size-5-tablet is-size-6-mobile has-text-weight-bold">
                                보통
                            </button>
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4-desktop is-size-5-tablet is-size-6-mobile has-text-weight-bold">
                                어려움
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns">
                <div class="column is-size-4 has-text-weight-bold">
                    대소문자 선택하기
                </div>
                <div class="column">
                    <div class="tile is-ancestor">
                        <div class="tile is-parent">
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4 has-text-weight-bold">
                                소문자
                            </button>
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4 has-text-weight-bold">
                                대문자
                            </button>
                        </div>

                    </div>
                </div>
            </div>
            <div class="columns">
                <div class="column is-size-4 has-text-weight-bold">
                    찾는 낱말의 철자 순서 섞기 (Scramble)
                </div>
                <div class="column">
                    <div class="tile is-ancestor">
                        <div class="tile is-parent">
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4 has-text-weight-bold">
                                예
                            </button>
                        </div>
                        <div class="tile is-parent">
                            <button
                                class="tile button is-child has-background-grey has-text-white is-size-4 has-text-weight-bold">
                                아니오
                            </button>
                        </div>

                    </div>
                </div>
            </div>
            <button type="submit" class="button is-info is-fullwidth is-size-1 has-text-weight-bold"
                id="make-worksheet">
                클릭하여 한글 파일로 다운로드 하기
            </button>
        </div>
    </section>
</template>

<style scoped lang="scss">
.button {
    border-radius: 20px;
}

#make-worksheet {
    border-radius: 0px;
}

.tile.is-child {
    padding: 10px;
}
</style>
