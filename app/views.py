import openpyxl
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import os
from django.conf import settings

# SOLO 3 CAMPOS
la_miel_mapping = {
    "fecha": "AN4",
    "ejecuto": "j5",
    "numero_ot": "J4"
}

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'daniel' and password == '88310462':
            return redirect('/app/main_menu/')
        else:
            return render(request, 'login/login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    return render(request, 'login/login.html')

def main_menu(request):
    return render(request, 'menu/main_menu.html')

def la_miel_list(request):
    if request.method == 'POST':
        print("=== INICIO POST ===")
        print("TODOS LOS DATOS POST:", dict(request.POST))  # Ver TODO lo que envía el form
        excel_template_path = "C:\\Users\\ANDRES\\Desktop\\la miel\\app\\templates\\EXEL\\PLT_201_MST_032_LA MIEL.xlsx"
        print("1. Buscando template Excel...")  # DEBUG
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_excel_file_name = f"{timestamp}_S30_LAMIEL.xlsx"
        excel_output_dir = os.path.join(settings.BASE_DIR, "EXCEL_GUARDADOS")
        os.makedirs(excel_output_dir, exist_ok=True)
        new_excel_file_path = os.path.join(excel_output_dir, new_excel_file_name)

        print("2. Cargando template Excel...")
        workbook = openpyxl.load_workbook(excel_template_path)
        print("3. Copiando template a nuevo archivo...")
        workbook.save(new_excel_file_path)

        print("4. Abriendo nuevo Excel...")
        workbook = openpyxl.load_workbook(new_excel_file_path)
        sheet = workbook['PLT_201_MST_032_ACT']
        print("5. Hoja encontrada: PLT_201_MST_032_ACT")

        try:
            print("6. Escribiendo datos en Excel...")
            for field_name, cell_ref in la_miel_mapping.items():
                value = request.POST.get(field_name)
                print(f"   Campo: {field_name} = {value}")
                if value:
                    sheet[cell_ref] = value
                    print(f"   OK Escrito en celda {cell_ref}")
            
            print("7. Guardando Excel...")
            workbook.save(new_excel_file_path)
            print(f"8. OK Excel guardado: {new_excel_file_path}")

            print("9. Preparando descarga...")
            with open(new_excel_file_path, 'rb') as excel_file:
                response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={new_excel_file_name}'
                return response

        except Exception as e:
            print(f"ERROR: {e}")  # DEBUG
            import traceback
            traceback.print_exc()  # DEBUG
            return render(request, 'subestacion/S30_LA_MIEL/s30_la_miel.html', {'error_message': f'Error al guardar y descargar Excel: {e}'})
    return render(request, 'subestacion/S30_LA_MIEL/s30_la_miel.html', {})
