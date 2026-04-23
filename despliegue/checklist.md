# Checklist de Despliegue - Viaticos-BanRep

Esta lista de verificación garantiza que cada despliegue a ambientes superiores (Test/Prod) sea consistente y libre de errores.

## 1. Pre-Despliegue (En Dev)
- [ ] Validar que todas las entidades custom tengan el prefijo `crb_`.
- [ ] Ejecutar el **Solution Checker** de Dataverse y resolver errores críticos.
- [ ] Asegurarse de que todos los flujos de Power Automate estén en estado "On".
- [ ] Verificar que no existan dependencias faltantes en la solución.
- [ ] Realizar un commit de los cambios actuales en la rama `feature/*`.

## 2. Ejecución del Deployment
- [ ] Ejecutar el pipeline `export-solution.yml` para actualizar el repositorio.
- [ ] Realizar Pull Request a la rama `main`.
- [ ] Verificar que el pipeline `import-to-test.yml` se dispare automáticamente.
- [ ] Confirmar que la importación en Test fue exitosa (Managed).

## 3. Post-Despliegue (En Test/Prod)
- [ ] Validar conexiones de los flujos de Power Automate (Connection References).
- [ ] Verificar que los Environment Variables tengan los valores correctos para el ambiente.
- [ ] Compartir la App con los grupos de seguridad correpondientes (Entra ID).
- [ ] Realizar una prueba de humo (Smoke Test) creando una solicitud de viáticos básica.

## 4. Aprobación Final
- [ ] Obtener visto bueno de UAT en ambiente de Test antes de promover a Prod.
- [ ] Ejecutar `import-to-prod.yml` y aprobar el Gate manual en Azure DevOps.
