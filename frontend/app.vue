<template>
  <n-config-provider :theme-overrides="themeOverrides">
    <n-message-provider>
      <div class="min-h-screen bg-white">
        <MainMenu />
        <NuxtPage />
      </div>
    </n-message-provider>
  </n-config-provider>
</template>

<script setup>
const themeOverrides = {
  common: {
    primaryColor: '#000000',
    primaryColorHover: '#333333',
    primaryColorPressed: '#666666'
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

body {
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

::selection {
  background: rgba(0, 0, 0, 0.1);
}

/* Transições globais */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}
</style>
