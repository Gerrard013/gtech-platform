# G Tech | Site Oficial 2.0 — Plano de redesign para aprovação
**13/11/2026 | Somente planejamento | NÃO publicar em produção**

## 1. Objetivo e decisões
- Transformar **o site oficial** em principal canal de descoberta, confiança, contato e venda para G Tech | Innovation & Solutions.
- Site oficial existente: `web-production-6f850.up.railway.app` (serviço Railway G tech plataforma).
- Preservar a aplicação atual e seus dados; redesenho em branch/staging, sem sobrescrever produção sem aprovação explícita.
- CRM principal existente `web-production-846ce.up.railway.app` é privado e será a origem dos leads e do pipeline.
- Loja independente existente `gtech-loja-online-production.up.railway.app` poderá fornecer catálogo/checkout validado ou ser integrada visualmente, **sem duplicar regras de pagamentos**.
- O link do Instagram `@gtech_brasil` só será apontado ao site oficial quando sua rota de contato estiver testada.

## 2. Diagnóstico do código atual
- Homepage atual focaliza educação, cursos, chat de IA e criação de conta: proposta distinta da venda imediata de NFC, sites, Google, soluções digitais.
- O formulário da página B2B grava `B2BLead` no banco da plataforma, não no CRM principal; requer validação end-to-end.
- Formularios autenticados/CSRF precisam de revisão e testes; não presumir que `POST /servicos-b2b/solicitar` funciona só porque GET funciona.
- A ativação de planos após retorno de checkout precisa ser substituída por verificação autenticada do status de pagamento; **bloquear fluxo atual de assinatura** até auditoria de segurança.
- Preservar serviço, autenticação, planos e cursos existentes somente quando fizerem sentido para o produto, sem eliminar nem migrar dados sem backup/decisão do CEO.
- Conferir segurança de cookies, logs, uploads, limites de requisição, consentimento LGPD, backup/restauração e alertas do Postgres.
- O site atual usa apenas uma logo local no diretório `app/static/img`. O email enviado trouxe **links** para seis vídeos, não os arquivos binários nem uma análise do conteúdo visual.

## 3. Direção visual sugerida
- **Conceito:** tecnologia premium, dark navy/preto-azulado, ciano elétrico, tipografia legível e efeitos discretos, sofisticados e rápidos.
- Abertura cinematográfica curta com vídeo real da G Tech se os materiais enviados forem aprovados. Logo e manchete legíveis; respeitar `prefers-reduced-motion`, controles de pausa e fallback estático.
- Priorizar mobile, qualidade e carregamento: vídeo de fundo comprimido, formato moderno quando possível, poster, lazy loading nas seções inferiores e sem áudio de reprodução automática.
- Não mostrar terceiros, clientes, telas de dados pessoais, marcas ou trilhas sem autorizações adequadas. Não copiar criativos ou interfaces de terceiros.

## 4. Wireframe do site de venda (sem vídeo final até avaliação das mídias)
1. **Header:** logotipo, Soluções, Projetos, Como funciona, Sobre, Contato | CTA fixo 'Solicitar orçamento'.
2. **Hero:** vídeo demonstrativo real + título 'Tecnologia que transforma presença em oportunidades' | subtítulo concreto | dois CTAs: 'Conhecer soluções' e 'Falar no WhatsApp'.
3. **Serviços:** NFC personalizado, Sites profissionais, Perfil da Empresa no Google, Restauração de fotos; sistemas e automações somente após alinhamento fiscal e escopo.
4. **Experiências/projetos:** demonstrações autorizadas, cases reais sem métricas inventadas, trailers curtos.
5. **Como funciona:** escolher → conversar → orçamento → aprovar → pagar → receber.
6. **Confiança:** perguntas frequentes, prazos/condições de entrega, depoimentos com autorização; sem avaliações falsas.
7. **Contato:** WhatsApp empresarial oficial (+55 91 98615-2222) e formulário simplificado integrado ao CRM.
8. **Rodapé:** razão social/identificação empresarial quando aplicável, políticas de privacidade e termos, contato e redes.

## 5. Jornada e integração
Instagram / busca / referências → **site oficial** → formulário / WhatsApp → **CRM único**
→ qualificação e IA Council consultiva → proposta humana → checkout oficial validado 
→ confirmação real de pagamento → produção/entrega → pós-venda.

### Critérios técnicos
- Cada formulário com origem/UTM, consentimento, rate limiting, honeypot, proteção CSRF adequada ao fluxo e tratamento de erros.
- CRM registra leads com idempotência/deduplicação, produto, origem, responsável e próxima ação. Nunca marcar como venda/paid sem verificação no gateway.
- Manter fornecedores/controle interno no CRM privado, não no site público.
- Definir componente de pagamento único (ou gateway específico por serviço), testar sandbox e confirmar recebedor.
- Metadados sociais/SEO, OpenGraph, favicon, acessibilidade, analytics consentidos e performance mobile.

## 6. Mídias enviadas (ainda não avaliadas visualmente)
O email `IMG_1110.eml` contém referências a:
- `ScreenRecording_08-03-2026 21-49-34_1.MP4`
- `ScreenRecording_08-06-2026 23-51-00_1.MP4`
- `IMG_1061.MOV`
- `IMG_1069.MOV`
- `IMG_1110.MOV`
- `IMG_1144.mov`

**Privacidade:** não guardar URLs Drive pessoais ou credenciais neste repositório público. O conteúdo dos vídeos só poderá ser classificado para hero, produtos, case ou Reels depois de acesso autorizado e inspeção de duração, resolução, áudio, consentimento e direitos de imagem.

## 7. Gate de aprovações (não avançar automaticamente)
- **Gate A:** Aprovar papel do site oficial e wireframe + estilo visual.
- **Gate B:** Analisar vídeos reais e aprovar cenas, cortes e localização de cada mídia.
- **Gate C:** Criar protótipo em branch com preview, sem alterar domínio/produção.
- **Gate D:** Revisão funcional e de segurança do formulário, conexão CRM e fluxo de pagamentos.
- **Gate E:** Teste mobile, acessibilidade, performance, SEO, analytics e restauração de backup.
- **Gate F:** CEO autoriza deploy; validar saúde após implantação; só então atualizar bio/link Instagram.

## 8. O que não fazer agora
- Não lançar código no `main` ou deploy.
- Não ativar pagamentos ou assinaturas antes de verificação de callbacks/webhooks.
- Não substituir banco, credenciais ou recursos legados.
- Não publicar vídeos sem revisar seu conteúdo e direitos.
- Não anunciar resultados de venda garantidos.

**Status:** plano inicial de arquitetura/UX; depende de aprovação de design, inspeção dos vídeos e testes técnicos.
