<template>
  <main class="content-wrapper">
    <h2 class="header">Dashboard</h2>

    <!-- Cards -->
    <div class="cards">
      <!-- Card -->
      <div class="card">
        <div class="card__img">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"
            ></path>
          </svg>
        </div>
        <div>
          <p class="card__title">Total clients</p>
          <p class="card__other">6389</p>
        </div>
      </div>
      <!-- Card -->
      <div class="card">
        <div class="card__img">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              fill-rule="evenodd"
              d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <div>
          <p class="card__title">Account balance</p>
          <p class="card__other">46,760.89</p>
        </div>
      </div>
      <!-- Card -->
      <div class="card">
        <div class="card__img">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"
            ></path>
          </svg>
        </div>
        <div>
          <p class="card__title">New sales</p>
          <p class="card__other">376</p>
        </div>
      </div>
      <!-- Card -->
      <div class="card">
        <div class="card__img">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              fill-rule="evenodd"
              d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <div>
          <p class="card__title">Pending contacts</p>
          <p class="card__other">35</p>
        </div>
      </div>

      <div class="card">
        <div class="card__img">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              fill-rule="evenodd"
              d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <div>
          <p class="card__title">Pending contacts</p>
          <p class="card__other">35</p>
        </div>
      </div>
    </div>

    <div class="user-list">
      <UserList />
    </div>
  </main>
</template>

<script>
  import UserList from "@/components/users/UserList.vue";

  export default {
    components: { UserList },
  };
</script>

<style lang="scss" scoped>
  .header {
    @apply my-6 text-2xl font-semibold text-gray-700 font-pt;
  }
  .content-wrapper {
    @apply container mx-auto px-6 pb-10 overflow-y-auto;
    scrollbar-width: thin;
    scrollbar-color: #9b9b9b transparent;
  }

  .cards {
    @apply grid gap-6 mb-8 <sm:gap-4 grid-cols-1 <sm:grid-cols-2 md:grid-cols-3
        lg:grid-cols-4;
  }
  .card {
    @apply flex items-center p-4 <sm:p-2 bg-light-100 rounded-lg shadow-sm;

    &__img {
      @apply <sm:p-1.85 p-3 mr-3 rounded-full text-brand-lime bg-lime-100;
    }
    &__title {
      @apply mb-1 text-base <sm:text-sm font-medium font-pt	text-gray-600;
    }
    &__other {
      @apply text-base font-semibold font-pt text-gray-700 <sm:text-sm;
    }
  }

  .user-list {
    @apply mb-10;
  }
</style>
