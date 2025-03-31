<template>
  <div class="min-h-screen flex flex-col relative px-4 md:px-0">
    <div class="w-full max-w-3xl mx-auto flex-grow pt-24">
      <h1 class="text-2xl font-medium mb-8 text-black/90">Configurações</h1>
      
      <!-- Configurações -->
      <div class="space-y-8">
        <!-- Aparência -->
        <section>
          <h2 class="text-lg font-medium mb-4 text-black/80">Aparência</h2>
          <n-form-item label="Tema" class="text-black/90">
            <n-select
              v-model:value="settings.theme"
              :options="[
                { label: 'Claro', value: 'light' },
                { label: 'Escuro', value: 'dark' },
                { label: 'Sistema', value: 'system' }
              ]"
            />
          </n-form-item>
        </section>

        <!-- Editor -->
        <section>
          <h2 class="text-lg font-medium mb-4 text-black/80">Editor</h2>
          <n-form-item label="Tamanho da fonte" class="text-black/90">
            <n-select
              v-model:value="settings.fontSize"
              :options="[
                { label: 'Pequeno', value: 'small' },
                { label: 'Médio', value: 'medium' },
                { label: 'Grande', value: 'large' }
              ]"
            />
          </n-form-item>
        </section>

        <!-- Notificações -->
        <section>
          <h2 class="text-lg font-medium mb-4 text-black/80">Notificações</h2>
          <n-space vertical>
            <n-switch v-model:value="settings.emailNotifications">
              <template #checked>Ativadas</template>
              <template #unchecked>Desativadas</template>
            </n-switch>
            <div class="text-sm text-black/60">
              Receber notificações por email sobre atualizações importantes
            </div>
          </n-space>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const settings = ref({
  theme: 'light',
  fontSize: 'medium',
  emailNotifications: true
})

// TODO: Integrar com backend para salvar configurações
watch(settings, (newSettings) => {
  console.log('Settings updated:', newSettings)
}, { deep: true })
</script>
