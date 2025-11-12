from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Usuario
    path('usuarios/', views.inicio_usuario, name='inicio_usuario'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/actualizar/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/realizar_actualizacion/<int:usuario_id>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    
    # URLs para Portafolio
    path('portafolios/', views.inicio_portafolio, name='inicio_portafolio'),
    path('portafolios/agregar/', views.agregar_portafolio, name='agregar_portafolio'),
    path('portafolios/actualizar/<int:portafolio_id>/', views.actualizar_portafolio, name='actualizar_portafolio'),
    path('portafolios/realizar_actualizacion/<int:portafolio_id>/', views.realizar_actualizacion_portafolio, name='realizar_actualizacion_portafolio'),
    path('portafolios/borrar/<int:portafolio_id>/', views.borrar_portafolio, name='borrar_portafolio'),
    
    # URLs para Activo
    path('activos/', views.inicio_activo, name='inicio_activo'),
    path('activos/agregar/', views.agregar_activo, name='agregar_activo'),
    path('activos/actualizar/<int:activo_id>/', views.actualizar_activo, name='actualizar_activo'),
    path('activos/realizar_actualizacion/<int:activo_id>/', views.realizar_actualizacion_activo, name='realizar_actualizacion_activo'),
    path('activos/borrar/<int:activo_id>/', views.borrar_activo, name='borrar_activo'),
    
    # URLs para Inversion
    path('inversiones/', views.inicio_inversion, name='inicio_inversion'),
    path('inversiones/agregar/', views.agregar_inversion, name='agregar_inversion'),
    path('inversiones/actualizar/<int:inversion_id>/', views.actualizar_inversion, name='actualizar_inversion'),
    path('inversiones/realizar_actualizacion/<int:inversion_id>/', views.realizar_actualizacion_inversion, name='realizar_actualizacion_inversion'),
    path('inversiones/borrar/<int:inversion_id>/', views.borrar_inversion, name='borrar_inversion'),
    
    # URLs para Transaccion
    path('transacciones/', views.inicio_transaccion, name='inicio_transaccion'),
    path('transacciones/agregar/', views.agregar_transaccion, name='agregar_transaccion'),
    path('transacciones/actualizar/<int:transaccion_id>/', views.actualizar_transaccion, name='actualizar_transaccion'),
    path('transacciones/realizar_actualizacion/<int:transaccion_id>/', views.realizar_actualizacion_transaccion, name='realizar_actualizacion_transaccion'),
    path('transacciones/borrar/<int:transaccion_id>/', views.borrar_transaccion, name='borrar_transaccion'),
]