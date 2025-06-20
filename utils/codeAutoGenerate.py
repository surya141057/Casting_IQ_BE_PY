import pandas as pd

class CodeAutoGenerate:
    @staticmethod
    def extract_numeric_part(s):
        if s is not None:
            numeric_part = ''.join(filter(str.isdigit, s))
            return int(numeric_part) if numeric_part else 0
        else:
            return 0

    @staticmethod
    def generator(model, prefix: str, key: str, is_draft: bool, slicer: int):
        filter_dict = {'is_draft': is_draft}
        if is_draft:
            filter_dict['is_active'] = True

        last_instance = model.objects.filter(**filter_dict)
        if last_instance.exists():
            df = pd.DataFrame(last_instance.values())
            max_code_alphanumeric = max(df[key], key=CodeAutoGenerate.extract_numeric_part)
        else:
            max_code_alphanumeric = None
        
        last_code = max_code_alphanumeric if max_code_alphanumeric and len(str(max_code_alphanumeric).strip()) > 0 else f'{prefix}0'
        suffix = last_code[slicer:]
        next_suffix = int(suffix) + 1 if suffix else 1
        return prefix, next_suffix

    @staticmethod
    def generate_code(model, attrs, prefix, id=None, key='code'):
        if 'is_draft' in attrs and attrs['is_draft'] == True:  # with draft changes
            if id:  # for PUT function
                if 'is_active' in attrs and attrs['is_active'] == False:
                    return attrs  # delete draft changes
                prefix, next_suffix = CodeAutoGenerate.generator(model, prefix, key, is_draft=False, slicer=len(prefix))
            else:
                prefix = f'TEMP{prefix}'
                prefix, next_suffix = CodeAutoGenerate.generator(model, prefix, key, is_draft=True, slicer=len(prefix))
        else:
            prefix, next_suffix = CodeAutoGenerate.generator(model,  prefix, key, is_draft=False, slicer=len(prefix))
            if id:  # for PUT function
                filter_dict = {'pk': id}
                individual_last_instance = model.objects.filter(**filter_dict).first()
                if 'is_active' in attrs and attrs['is_active'] == False:
                    return attrs  # delete changes
                if individual_last_instance and hasattr(individual_last_instance, key) and getattr(individual_last_instance, key)[:len(prefix)] == prefix:
                    return attrs

        code = f"{prefix}{next_suffix:03d}"
        attrs[key] = code
        return attrs
