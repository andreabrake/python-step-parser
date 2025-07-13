strval = "GEOMETRIC_REPRESENTATION_CONTEXT(3) GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#543338)) GLOBAL_UNIT_ASSIGNED_CONTEXT((#543341,#543340,#543339)) REPRESENTATION_CONTEXT('91172GT01202Z9-006','COMPONENT_PART')"

entities = []
state = 0
curr_entity = []

for v in strval:
    curr_entity.append(v)

    if state == 0:
        if v == '(':
            state = 1
    elif state > 0:
        if state == 1 and v == ')':
            entities.append(''.join(curr_entity).strip())
            curr_entity = []
            state = 0
        elif v == '(':
            state += 1
        elif v == ')':
            state -= 1
        
print(entities)